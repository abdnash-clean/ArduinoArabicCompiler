# Backend Layer Plan — Targeting the Arduino CPU (AVR / ATmega328P)

> A detailed, lab-style guide for building the **back-end** of the Arduino-Arabic
> compiler. It mirrors the course labs (20, 22–24) but **retargets everything
> from the host CPU (x86/ARM) to the AVR ATmega328P** used by the Arduino
> Uno / Nano.
>
> Audience: the teammate doing the back-end. The middle-end (IR generation +
> optimization) is already done. The optimizer already emits AVR objects via
> `backend/optimizer.py` (`emit_object` / `write_object`).
>
> **Scope note:** the dynamic-heap lab (Lab 25) and the terminal-I/O lab
> (Lab 26) are intentionally **excluded** — they don’t fit a 2 KB-RAM, no-OS
> microcontroller. The empathetic-compiler / AI-mentor / TDD lab (Lab 28) is a
> developer-experience concern and is covered in the separate
> **`IDE_INTEGRATION_GUIDE.md`**.

---

## 0. The single most important idea

The labs assume the program will run **on your computer**, talking to the
operating system (`printf`, `main`, an `.exe`). **An Arduino has no operating
system.** There is no `printf` to a screen, no process `main`. Instead:

- Output goes over the **UART/Serial** line (`Serial.print`), not stdout.
- The entry points are **`setup()` once + `loop()` forever**, started by the
  Arduino core, not an OS.
- The final artifact is a **`.hex`** image **flashed** into 32 KB of flash with
  `avrdude` — not a double-clickable executable.
- When something goes catastrophically wrong (e.g. divide-by-zero), there is no
  `exit()` to an OS — the safe move is to **announce over Serial and halt**.

So the back-end’s job is: optimized LLVM IR → **AVR** object file → **link with
the Arduino core + a small glue layer (including the panic handler)** → `.elf`
→ `.hex` → flash.

---

## 1. What changes vs the labs (cheat sheet)

| Step | Lab (host CPU) | Our target (AVR ATmega328P) |
|---|---|---|
| Init | `initialize_native_target()` | `initialize_all_targets()` (AVR is a *cross* target; native init does NOT register it) |
| Triple | `get_default_triple()` | `"avr-atmel-none"` |
| CPU | default | `"atmega328p"` |
| TargetMachine | `create_target_machine()` | `create_target_machine(cpu="atmega328p", reloc="static", codemodel="small")` |
| Data layout | host data layout | `e-P1-p:16:8-i8:8-i16:8-i32:8-i64:8-f32:8-f64:8-n8-a:8` (16-bit pointers) |
| `int` width | 32/64-bit | **16-bit** (`long` = 32-bit) |
| Object | `emit_object` → `.o` | same API, but AVR machine code |
| Disassemble | `objdump -d` | `avr-objdump -d` |
| Linker | `gcc out.o runtime.c` | `avr-g++ out.o glue.cpp core.a -mmcu=atmega328p` |
| Runtime lib | `runtime.c` (printf/exit) | `arduino_glue.cpp` (wraps `pinMode`/`digitalWrite`/`Serial`… + `panic_div_zero`) + Arduino core |
| Entry point | OS `main()` | own `main()` → `init()` → `setup()` → `loop()` |
| Output / run | `.exe`, run directly | `.hex`, `avrdude` flash, watch Serial Monitor |
| Print | `printf` to stdout | `Serial.print` over UART |
| Panic (div/0) | `printf` + `exit(1)` | `Serial.println` + `cli()` + infinite halt (no OS to exit to) |

---

## 2. Prerequisites the friend must install

1. **llvmlite 0.47 with the AVR backend compiled in.** Verify (fresh process):
   ```python
   import llvmlite.binding as llvm
   llvm.initialize_all_targets()         # NOT initialize_native_target()
   llvm.initialize_all_asmprinters()
   print(llvm.Target.from_triple("avr-atmel-none"))
   # -> <Target avr (Atmel AVR Microcontroller)>  ✅
   ```
   If this raises *"no targets are registered"*, the registration call is
   missing. If it raises *"No available targets…"*, this llvmlite build has no
   AVR backend → use the external-toolchain fallback (§9).
2. **AVR toolchain**: `avr-gcc`, `avr-g++`, `avr-objcopy`, `avr-objdump`,
   `avr-size` — easiest via **arduino-cli** (`arduino-cli core install arduino:avr`)
   or the Arduino IDE, or a system package (`gcc-avr avr-libc binutils-avr`).
3. **avrdude** (ships with the Arduino toolchain) for flashing.
4. The **optimized IR** string from the middle-end (`ir_gen.get_ir()` after
   `Optimizer(...).optimize(...)`).

---

## 3. Session B1 — Target Machine Setup for AVR  *(adapts Lab 22)*

The lab’s `initialize_target_machine()` queries the host. Replace it with a
fixed AVR target. Put this in `backend/avr_target.py` (or inside `main.py`).

```python
import llvmlite.binding as llvm

AVR_TRIPLE = "avr-atmel-none"
AVR_CPU = "atmega328p"
# 16-bit pointers, byte alignment — this is what makes the back-end size structs
# and pointers correctly for an 8-bit MCU.
AVR_DATALAYOUT = "e-P1-p:16:8-i8:8-i16:8-i32:8-i64:8-f32:8-f64:8-n8-a:8"

_initialized = False

def initialize_avr_target_machine(opt_level=2):
    global _initialized
    if not _initialized:
        # AVR is a CROSS target. The deprecated initialize()/initialize_native_*
        # only set up the host. We must register ALL targets.
        llvm.initialize_all_targets()
        llvm.initialize_all_asmprinters()
        _initialized = True

    target = llvm.Target.from_triple(AVR_TRIPLE)
    target_machine = target.create_target_machine(
        cpu=AVR_CPU,
        features="",
        opt=opt_level,
        reloc="static",      # MCUs don't use position-independent code
        codemodel="small",
    )
    print(f"\U0001F3AF Target architecture: {AVR_TRIPLE} (cpu={AVR_CPU})")
    return target_machine, AVR_TRIPLE
```

Then bind the module to the target (Lab 22, Step 2 — the “critical architecture
step”), but use the **AVR** triple and data layout:

```python
mod = llvm.parse_assembly(optimized_llvm_ir)
mod.verify()
mod.triple = AVR_TRIPLE
mod.data_layout = str(target_machine.target_data)   # AVR data layout
```

> If you already run optimization through `backend/optimizer.py`, it sets the
> triple/data layout and registers targets for you — reuse it instead of
> duplicating logic.

**Engineering audit (B1)**
- Does it print `avr-atmel-none` (not your PC’s triple)? ✅
- In a fresh process, does `from_triple("avr-atmel-none")` succeed? ✅
- Is `mod.data_layout` the 16-bit-pointer AVR layout? ✅

---

## 4. Session B2 — Emit Assembly for inspection  *(adapts Lab 22, Step 3)*

Same API as the lab, but the output is **AVR assembly**, not x86.

```python
asm = target_machine.emit_assembly(mod)
with open("output.s", "w", encoding="utf-8") as f:
    f.write(asm)
```

**Engineering audit (B2)** — open `output.s` and confirm you see **AVR**
mnemonics, not Intel/ARM:
- AVR instructions: `ldi`, `mov`, `add`, `rcall`/`call`, `rjmp`, `ret`,
  `sbi`/`cbi` (set/clear I/O bit), `in`/`out`, `lds`/`sts`.
- AVR registers: `r24`, `r25`, `r18`… (8-bit regs, often paired like `r25:r24`
  for a 16-bit value). **No** `%rax`/`%rsp` (x86) and **no** `x0/sp` (ARM).
- The `.arch atmega328p` / device directives at the top.
- Note how a 16-bit `int` lives in a **register pair** — that’s the 8-bit reality.

---

## 5. Session B3 — Emit the Object File (.o)  *(adapts Lab 23)*

Text → bytes. Open the file in **binary** mode (`wb`).

```python
obj = target_machine.emit_object(mod)   # runs InstrSel + RegAlloc for AVR
with open("output.o", "wb") as f:
    f.write(obj)
print("\u2705 output.o (AVR object) generated")
```

Inspect with the **AVR** disassembler (not plain `objdump`):
```bash
avr-objdump -d output.o
```

**Engineering audit (B3)**
- Is `output.o` bigger than zero bytes? ✅
- Does `avr-objdump -d` show AVR opcodes and that the Arabic variables became
  physical registers? ✅
- Are there **unresolved symbols** (`pinMode`, `digitalWrite`, `c_delay`,
  `panic_div_zero`, `setup`, `loop`, …)? **Yes, expected** — they get resolved
  at link time in B6.
- Is it runnable? **No** — it’s raw material, exactly like the lab said.

---

## 6. Session B4 — The Runtime Glue  *(replaces Lab 24’s `runtime.c`)*

This is the biggest conceptual change. The lab’s `runtime.c` provides
`panic_div_zero` and uses `printf`. On AVR there is no `printf` to a screen and
no OS `main`. Instead, your generated IR only **declares** functions like
`c_pinMode`, `c_digitalWrite`, `c_delay`, `c_serialBegin`, `panic_div_zero`,
… — something must **define** them by calling the real **Arduino core**.

Create `runtime/arduino_glue.cpp` (already generated for you in this project):

```cpp
#include <Arduino.h>
#include <stdint.h>

extern "C" {
    void setup();   // اعداد  (generated by your compiler)
    void loop();    // تكرار  (generated by your compiler)

    // ⚠️ ABI: on AVR `int` is 16-bit but your language's "صحيح" is i32,
    // so EVERY wrapper uses int32_t to match argument passing.
    void    c_pinMode(int32_t p, int32_t m)     { pinMode((uint8_t)p, (uint8_t)m); }
    void    c_digitalWrite(int32_t p, int32_t v){ digitalWrite((uint8_t)p, (uint8_t)v); }
    int32_t c_digitalRead(int32_t p)            { return (int32_t)digitalRead((uint8_t)p); }
    void    c_analogWrite(int32_t p, int32_t v) { analogWrite((uint8_t)p, (int)v); }
    int32_t c_analogRead(int32_t p)             { return (int32_t)analogRead((uint8_t)p); }
    void    c_delay(int32_t ms)                 { delay((uint32_t)ms); }
    int32_t c_millis()                          { return (int32_t)millis(); }
    void    c_serialBegin(int32_t baud)         { Serial.begin((long)baud); }
    void    c_serialPrintInt(int32_t v)         { Serial.println(v); }
}

// Our own entry point. We do NOT link Arduino's main.cpp (it expects
// C++-mangled setup/loop; ours are C-linkage). init() configures the timers
// that delay()/millis()/PWM rely on — do not skip it.
int main(void) {
    init();
    setup();
    for (;;) {
        loop();
        if (serialEventRun) serialEventRun();
    }
}
```

**Three real gotchas (must understand):**
1. **`int` is 16-bit on AVR.** Your “صحيح” is i32. If a wrapper uses `int`
   instead of `int32_t`, arguments are silently mis-passed. (Handled above.)
2. **`setup`/`loop` linkage.** Arduino’s own `main.cpp` expects C++-mangled
   names; your compiler emits C names. We provide our own `main` + `extern "C"`
   and don’t link Arduino’s `main.cpp`.
3. **LLVM↔avr-gcc ABI** is compatible for simple integer args, but not
   guaranteed for floats/variadic/structs. Test with a blink first.

> **Registers need no glue.** Direct register access (`منفذ_ب`, `اتجاه_ب`…)
> compiles to volatile loads/stores at the same memory addresses avr-libc uses
> (PORTB=0x25, DDRB=0x24, …), so it works after linking with no wrapper.

---

## 7. Session B5 — Runtime Safety Traps on AVR  *(adapts Lab 20)*

Lab 20 makes the compiler inject a divide-by-zero guard: the **middle-end**
emits an `icmp eq` against 0, a conditional branch to a `panic_block` that
`call`s `panic_div_zero()` then `unreachable`, and a `math_block` that does the
safe `sdiv`. **That IR is already generated by your middle-end — nothing
changes there.** What changes is the *definition* of `panic_div_zero`, which is
a back-end / runtime concern and lives in the glue.

The lab’s handler does `printf(...)` + `exit(1)`. On a microcontroller there is
no console and nowhere to “exit” to, so the safe behavior is: **announce over
Serial, then halt the CPU** (optionally blink the on-board LED as a fault
beacon). Add this to `runtime/arduino_glue.cpp`:

```cpp
#include <avr/interrupt.h>   // for cli()

extern "C" void panic_div_zero() {
    // 1) Announce (only meaningful if the sketch called Serial.begin in setup).
    Serial.println(F("[Runtime Error] Division by zero! Program halted safely."));
    Serial.flush();          // make sure the bytes leave before we freeze

    // 2) Halt: there is no OS to exit() to. Stop interrupts and freeze.
    cli();
    pinMode(13, OUTPUT);     // PB5 / on-board LED as a visible fault code
    for (;;) {
        digitalWrite(13, HIGH); for (volatile long i=0;i<150000;i++);
        digitalWrite(13, LOW);  for (volatile long i=0;i<150000;i++);
    }
}
```

Keep the IR contract identical to the lab so optimization still reasons about
it:

```llvm
  %is_zero_trap = icmp eq i32 %den, 0
  br i1 %is_zero_trap, label %panic_block, label %math_block
panic_block:
  call void @panic_div_zero()
  unreachable
math_block:
  %divtmp = sdiv i32 %num, %den
```

**Why `unreachable` is still correct on AVR:** `panic_div_zero` never returns
(infinite loop), so marking the block `unreachable` is truthful and lets the
optimizer keep proving things (exactly like Lab 21: if the optimizer can prove
the denominator is non-zero, it deletes the whole trap).

**Engineering audit (B5)**
- Does the linked firmware still contain `panic_div_zero` (`avr-objdump -d`),
  unless the optimizer proved it unreachable and removed it? ✅
- On a real divide-by-zero, does the board print the message (if Serial was
  started) and then blink/halt instead of behaving randomly? ✅
- Did you avoid `exit()`/`abort()` (they just spin on AVR and waste flash)? ✅

---

## 8. Session B6 — Link → ELF → HEX  *(adapts Lab 24, Steps 2–3)*

The lab does `gcc output.o runtime.c -o app.exe`. On AVR we need `avr-g++`, the
`-mmcu` flag, the Arduino core, and a separate objcopy to make a `.hex`.

### 8.1 Get the Arduino core (one-time)
```bash
arduino-cli core install arduino:avr
# core source:   .../packages/arduino/hardware/avr/<ver>/cores/arduino
# variant pins:  .../packages/arduino/hardware/avr/<ver>/variants/standard
# toolchain bin: .../packages/arduino/tools/avr-gcc/<ver>/bin
```
Build the core once into `core.a` (compile every `.c`/`.cpp` in `cores/arduino`
with `-mmcu=atmega328p -DF_CPU=16000000L -Os -I<core> -I<variant>`, then
`avr-gcc-ar rcs core.a *.o`). Tip: compiling any sketch once with arduino-cli
leaves a ready `core.a` in its build temp folder — you can copy it.

### 8.2 Compile glue + link
```bash
MCU=atmega328p
FCPU=16000000L
CORE=.../cores/arduino
VAR=.../variants/standard

# compile the glue (now also contains panic_div_zero)
avr-g++ -mmcu=$MCU -DF_CPU=$FCPU -Os -ffunction-sections -fdata-sections \
    -I"$CORE" -I"$VAR" -c runtime/arduino_glue.cpp -o arduino_glue.o

# link: your program + glue + Arduino core
avr-g++ -mmcu=$MCU -Os -Wl,--gc-sections \
    output.o arduino_glue.o core.a -o firmware.elf

# size report (watch flash <= 32 KB, RAM <= 2 KB)
avr-size --mcu=$MCU -C firmware.elf

# ELF -> Intel HEX
avr-objcopy -O ihex -R .eeprom firmware.elf firmware.hex
```

### 8.3 Automate it from `main.py` (adapts Lab 24’s `link_and_run`)
```python
import subprocess

def link_and_flash(obj="output.o", glue="runtime/arduino_glue.cpp",
                   core="core.a", core_inc="", var_inc="",
                   mcu="atmega328p", fcpu="16000000L",
                   port="/dev/ttyACM0", baud="115200", do_flash=False):
    # 1) compile glue
    subprocess.run(["avr-g++", f"-mmcu={mcu}", f"-DF_CPU={fcpu}", "-Os",
                    "-ffunction-sections", "-fdata-sections",
                    f"-I{core_inc}", f"-I{var_inc}",
                    "-c", glue, "-o", "arduino_glue.o"], check=True)
    # 2) link
    subprocess.run(["avr-g++", f"-mmcu={mcu}", "-Os", "-Wl,--gc-sections",
                    obj, "arduino_glue.o", core, "-o", "firmware.elf"], check=True)
    # 3) hex
    subprocess.run(["avr-objcopy", "-O", "ihex", "-R", ".eeprom",
                    "firmware.elf", "firmware.hex"], check=True)
    print("\u2705 firmware.hex ready")
    # 4) optional flash
    if do_flash:
        subprocess.run(["avrdude", "-c", "arduino", "-p", mcu,
                        "-P", port, "-b", baud,
                        "-U", "flash:w:firmware.hex:i"], check=True)
        print("\u2705 flashed to board")
```

**Engineering audit (B6)**
- Did linking finish with **no “undefined reference”**? (If `setup`/`loop` are
  undefined, your IR didn’t emit them with C linkage; if `c_*` / `panic_div_zero`
  are undefined, the glue isn’t compiled/linked.) ✅
- Does `avr-size` show flash ≤ 32256 bytes and RAM ≤ 2048 bytes? ✅
- Did `firmware.hex` get created and start with `:` lines (Intel HEX)? ✅

---

## 9. Session B7 — Flash & run on hardware  *(replaces “run the .exe”)*

```bash
avrdude -c arduino -p atmega328p -P /dev/ttyACM0 -b 115200 \
        -U flash:w:firmware.hex:i
```
- On Linux the port is usually `/dev/ttyACM0` or `/dev/ttyUSB0`; on Windows
  `COM3` etc.; on macOS `/dev/cu.usbmodemXXXX`.
- Old bootloaders (real ATmega328P / Nano clones) may need `-b 57600`.

**There is no stdout.** To “see” output, the Arabic program must use Serial, and
you open the **Serial Monitor** at the matching baud:
```bash
arduino-cli monitor -p /dev/ttyACM0 --config baudrate=9600
```
A good first test is the register/blink example (toggle PORTB5 = pin 13) — if
the on-board LED blinks, the whole back-end chain works end to end. Then test a
divide-by-zero sketch and confirm the panic message + halt from §7.

### Fallback if this llvmlite build has **no** AVR backend
Optimization still works (target-independent). Emit the optimized **`.ll`** and
let an external toolchain do codegen + link:
```bash
llc -mtriple=avr -mcpu=atmega328p -filetype=obj program.ll -o output.o
# then the same B6/B7 steps
```
(or hand the `.ll` to `clang --target=avr` / let `avr-gcc` assemble a `.s`).

---

## 10. Putting the back-end together (`main.py` flow)

```python
# --- front-end + middle-end (already done) ---
raw_ir = ir_gen.get_ir()

# --- middle-end optimization (already done) ---
from backend.optimizer import Optimizer
optimized_ir = Optimizer(opt_level=2, size_level=1, verbose=True).optimize(raw_ir)

# --- BACK-END (this plan) ---
from backend.avr_target import initialize_avr_target_machine
import llvmlite.binding as llvm

tm, triple = initialize_avr_target_machine(opt_level=2)
mod = llvm.parse_assembly(optimized_ir)
mod.verify()
mod.triple = triple
mod.data_layout = str(tm.target_data)

# B2 (optional) assembly for inspection
open("output.s", "w", encoding="utf-8").write(tm.emit_assembly(mod))
# B3 object
open("output.o", "wb").write(tm.emit_object(mod))
# B6/B7 link + hex (+ optional flash); panic_div_zero comes from the glue
link_and_flash(do_flash=False)
```

---

## 11. AVR-specific pitfalls checklist

- [ ] Used `initialize_all_targets()` (NOT `initialize_native_target()`).
- [ ] Triple `avr-atmel-none`, CPU `atmega328p`, `reloc="static"`, `codemodel="small"`.
- [ ] Module `data_layout` set to the AVR (16-bit pointer) layout.
- [ ] Glue wrappers use `int32_t` (not `int`) to match the i32 ABI.
- [ ] `panic_div_zero` defined in the glue as Serial-announce + `cli()` + halt
      (NOT `exit()`); IR keeps the `call` + `unreachable` contract.
- [ ] Provided our own `main()` calling `init()` → `setup()` → `loop()`; did NOT
      link Arduino’s `main.cpp`.
- [ ] Linked with `avr-g++ -mmcu=atmega328p` + `core.a` (not `gcc`).
- [ ] `-DF_CPU=16000000L` set, so `delay()`/`millis()` timing is correct.
- [ ] `Serial.begin()` in setup before printing; matching baud in the monitor.
- [ ] Float printing over Serial uses `Serial.print(float)` (avoid `printf %f`).
- [ ] Checked `avr-size`: flash ≤ 32 KB, SRAM ≤ 2 KB.
- [ ] Tested blink/Serial “hello”, then a divide-by-zero, before trusting complex
      programs (validates the ABI and the panic path on real hardware).

---

## 12. Suggested file layout

```
backend/
  optimizer.py        # middle-end (done) — also has emit_object/emit_assembly
  avr_target.py       # B1: AVR target machine setup
  codegen.py          # B2/B3: emit .s and .o
  linker.py           # B6/B7: link_and_flash()
runtime/
  arduino_glue.cpp    # B4 + B5: c_* wrappers, panic_div_zero, main()/setup()/loop()
core.a                # prebuilt Arduino core (from arduino-cli)
```

That’s the whole back-end: **AVR target → object → glue + core link (with the
AVR panic handler) → hex → flash**, with Serial as the I/O channel and a hard
2 KB RAM budget to respect.

> Developer experience (friendly Arabic error messages via the AI mentor, and
> the automated-test harness from Lab 28) is **not** a back-end task — it lives
> in **`IDE_INTEGRATION_GUIDE.md`**, which the IDE teammate owns.
