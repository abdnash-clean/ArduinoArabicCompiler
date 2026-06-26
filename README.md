# Arduino Arabic Compiler

A Python-based compiler that translates **Arabic Arduino-style source code** into LLVM IR, optimizes it for AVR, and produces a `firmware.hex` file ready to flash onto an Arduino Uno (ATmega328P).

> 🌐 **Language**: Arabic keywords and built-ins.
> ⚙️ **Backend**: LLVM IR → AVR assembly/object → Intel HEX.
> 🔌 **Hardware**: Arduino Uno and compatible ATmega328P boards.

---

## What is this?

The **Arduino Arabic Compiler** allows users to write Arduino programs using Arabic keywords and built-in function names. It is a complete compiler pipeline:

```text
Arabic source code
   ↓
Lexer + Parser (ANTLR4)
   ↓
Abstract Syntax Tree (AST)
   ↓
Semantic Analysis
   ↓
LLVM IR Generation
   ↓
Optimization + AVR Codegen
   ↓
Linking → firmware.hex
   ↓
Flash to Arduino Uno
```

The compiler is designed to be driven by the Flutter IDE in `IDE/`, but it can also be used standalone from the command line.

---

## Features

- ✅ Arabic keywords and built-in names
- ✅ Arabic text normalization (tashkeel, hamza variants, tatweel)
- ✅ Full lexer/parser with ANTLR4
- ✅ AST construction with visitor pattern
- ✅ Semantic analysis with scope and type checking
- ✅ LLVM IR generation targeting AVR
- ✅ AVR optimization and object code emission
- ✅ Linker that produces `firmware.hex`
- ✅ Flash support via `avrdude`
- ✅ Serial library support
- ✅ Runtime panic handler (e.g., division by zero)
- ✅ Sample programs: blink, serial hello, panic test

---

## Getting Started

### Prerequisites

- Python 3 (tested on 3.14)
- Git
- (Optional) Java, if regenerating ANTLR files from grammars
- (Optional) Arduino Uno for hardware testing

### Installation

1. Open a terminal in the `ArduinoArabicCompiler/` directory.

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Install dependencies:

   ```bash
   # Windows
   .venv\Scripts\pip install -r requirements.txt

   # Linux / macOS
   # .venv/bin/pip install -r requirements.txt
   ```

4. Verify AVR support:

   ```bash
   .venv\Scripts\python -c "import llvmlite.binding as llvm; print(llvm.Target.from_triple('avr-atmel-none'))"
   ```

   Expected output:

   ```text
   <Target avr (Atmel AVR Microcontroller)>
   ```

5. Set up the AVR toolchain and build the Arduino core library:

   ```bash
   python build.py setup
   ```

### Compile the default sample

```bash
python build.py compile
```

This reads `test_arduino.txt` and produces:

- `output.o` — AVR object file
- `output.s` — AVR assembly listing
- `firmware.hex` — Intel HEX file ready for flashing

### Run tests

```bash
python build.py test
```

### Flash to Arduino

```bash
# Windows
python build.py flash COM3

# Linux
python build.py flash /dev/ttyACM0
```

---

## Example Program

```arabic
استيراد "سيريال" ؛

دالة اعداد():فارغ {
    وضع_الطرف(13, مخرج);
    سيريال_ابدا(9600);
}

دالة تكرار():فارغ {
    اكتب_رقمي(13, عالي);
    انتظر(1000);
    اكتب_رقمي(13, منخفض);
    انتظر(1000);
    سيريال_اطبع("مرحباً من Arduino!");
}
```

Save this as `test_arduino.txt`, then run:

```bash
python build.py compile
python build.py flash COM3
```

---

## Project Structure

```text
ArduinoArabicCompiler/
├── main.py                 # Compiler driver
├── build.py                # Build helper
├── normlize.py             # Arabic text normalization
├── frontend/               # Lexer/parser grammar and AST builder
├── ast_dir/                # AST node definitions and visitor interface
├── semantic/               # Semantic analyzer, types, symbols, built-ins
├── backend/                # IR generator, optimizer, AVR codegen, linker
├── runtime/                # C++ runtime wrappers and panic handler
├── tools/                  # Toolchain setup and Arduino CLI
├── samples/                # Example programs
├── docs/                   # Architecture and integration docs
└── guide_docs/             # Developer guides
```

---

## Build Commands

`build.py` provides a unified interface for common tasks:

```bash
python build.py setup       # Install toolchain and build core.a (one-time)
python build.py compile     # Compile test_arduino.txt
python build.py test        # Run backend tests
python build.py link        # Link output.o into firmware.hex
python build.py flash       # Flash firmware.hex to Arduino
python build.py ports       # List connected boards/ports
python build.py monitor     # Open serial monitor bridge for the IDE
python build.py clean       # Remove generated files
```

---

## IDE Integration

The compiler is designed to be driven by the Flutter IDE. The IDE should:

1. Call the compiler as a subprocess.
2. Parse compiler output and diagnostics.
3. Render IR, assembly, and error panels.
4. Use `build.py flash` and `build.py monitor` for hardware interaction.

See `docs/IDE_INTEGRATION_GUIDE.md` for the full integration contract.

---

## Development

For detailed developer documentation, see:

📄 [`guide_docs/COMPILER_DEVELOPER_GUIDE.md`](guide_docs/COMPILER_DEVELOPER_GUIDE.md)

It covers:

- The full compiler pipeline
- How to add language features
- How to extend the backend
- How to add built-in functions
- Testing strategy
- Troubleshooting
- Code style conventions

### Quick commands

```bash
python build.py compile    # Compile default sample
python build.py test       # Run backend tests
python build.py flash COM3 # Flash to Arduino
python build.py clean      # Clean generated files
```

---

## Samples

| Sample | Purpose |
|--------|---------|
| `samples/blink.txt` | Blinks the onboard LED on pin 13. |
| `samples/serial_hello.txt` | Prints messages over Serial. |
| `samples/panic_test.txt` | Tests division-by-zero panic handler. |
| `test_arduino.txt` | Complex autonomous robot controller. |

To try a sample:

```bash
cp samples/blink.txt test_arduino.txt
python build.py compile
python build.py flash COM3
```

---

## Contributing

Contributions are welcome! Please:

1. Read the compiler developer guide.
2. Use normalized Arabic names (ا only, no أ/إ/آ) for built-ins.
3. Update all AST visitors when adding new node types.
4. Add tests for new features.
5. Run `python build.py test` before submitting changes.

---

## License

This project is part of the Arabic Arduino IDE workspace. See the repository license for details.

---

## Support

If you encounter issues:

- Check the troubleshooting section in the developer guide.
- Verify your `llvmlite` installation supports AVR.
- Ensure the Arduino toolchain is installed (`python build.py setup`).
- Check your board drivers if the port is not detected.
