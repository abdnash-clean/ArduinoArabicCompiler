# Arduino Arabic Compiler — Developer Guide

> A comprehensive guide for developers who want to run, understand, extend, or contribute to the **Arabic Arduino Compiler** in `ArduinoArabicCompiler/`.

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [What You Will Build](#2-what-you-will-build)
3. [Prerequisites](#3-prerequisites)
4. [Getting Started](#4-getting-started)
5. [Project Structure](#5-project-structure)
6. [Architecture Deep Dive](#6-architecture-deep-dive)
7. [Feature Areas You Can Develop](#7-feature-areas-you-can-develop)
8. [Step-by-Step Development Workflows](#8-step-by-step-development-workflows)
9. [Language Reference](#9-language-reference)
10. [Code Style and Conventions](#10-code-style-and-conventions)
11. [Testing Strategy](#11-testing-strategy)
12. [Troubleshooting](#12-troubleshooting)
13. [Performance and Best Practices](#13-performance-and-best-practices)
14. [Security and Safety Notes](#14-security-and-safety-notes)
15. [FAQ](#15-faq)
16. [References and Next Steps](#16-references-and-next-steps)

---

## 1. Introduction

The `ArduinoArabicCompiler/` directory contains a complete compiler pipeline that turns **Arabic Arduino-style source code** into firmware that can run on an Arduino Uno (ATmega328P). It is written in Python and uses:

- **ANTLR4** for lexical analysis and parsing.
- **A custom AST** built with visitor classes.
- **Semantic analysis** with symbol tables and type checking.
- **LLVM IR** generation via `llvmlite`.
- **AVR backend** for optimization, assembly, object code, linking, and flashing.

This guide explains how to set up the project, how each compiler stage works, and where to add new language features or backend capabilities.

---

## 2. What You Will Build

As a compiler developer, you are extending a programming language designed for Arabic speakers. Your work enables users to write Arduino programs using Arabic keywords, compile them to real AVR machine code, and upload them to hardware.

### Example user program

```arabic
استيراد "سيريال" ؛

متغير العداد : صحيح = 0 ؛

دالة اعداد():فارغ {
    وضع_الطرف(13, مخرج);
    سيريال_ابدا(9600);
}

دالة تكرار():فارغ {
    اكتب_رقمي(13, عالي);
    انتظر(1000);
    اكتب_رقمي(13, منخفض);
    انتظر(1000);
    العداد = العداد + 1 ؛
    سيريال_اطبع(العداد);
}
```

This program blinks the onboard LED and prints a counter over Serial.

---

## 3. Prerequisites

### Required

- Python 3 (tested on 3.14; exact version may be limited by `llvmlite` wheels)
- Git

### Recommended

- A C++ compiler for building `arduino_glue.cpp` and `core.a`
- Java, if you plan to regenerate ANTLR files from `.g4` grammars

### Optional

- An Arduino Uno or compatible ATmega328P board for hardware testing
- A USB A-to-B cable

---

## 4. Getting Started

All commands below assume your terminal is inside the `ArduinoArabicCompiler/` directory.

### 4.1 Create a virtual environment

```bash
python -m venv .venv
```

### 4.2 Install dependencies

```bash
# Windows
.venv\Scripts\pip install -r requirements.txt

# Linux / macOS
# .venv/bin/pip install -r requirements.txt
```

Dependencies:

```text
antlr4-python3-runtime==4.13.2
llvmlite==0.47.0
```

### 4.3 Verify AVR support

```bash
.venv\Scripts\python -c "import llvmlite.binding as llvm; print(llvm.Target.from_triple('avr-atmel-none'))"
```

Expected:

```text
<Target avr (Atmel AVR Microcontroller)>
```

### 4.4 One-time AVR toolchain setup

```bash
python build.py setup
```

This downloads the Arduino CLI and builds `runtime/core.a`.

### 4.5 Compile the default sample

```bash
python build.py compile
```

This reads `test_arduino.txt` and produces:

- `output.o` — AVR object file
- `output.s` — AVR assembly listing
- `firmware.hex` — Intel HEX file ready for flashing

### 4.6 Run tests

```bash
python build.py test
```

### 4.7 Flash to hardware

```bash
python build.py flash COM3        # Windows
python build.py flash /dev/ttyACM0 # Linux
```

### 4.8 Clean generated files

```bash
python build.py clean
```

### 4.9 Manual compilation (without build.py)

```bash
set PYTHONIOENCODING=utf-8
python main.py
```

> `main.py` is currently hardcoded to read `test_arduino.txt`.

---

## 5. Project Structure

```text
ArduinoArabicCompiler/
├── main.py                          # Compiler driver
├── build.py                         # Build helper
├── normlize.py                      # Arabic text normalization
├── ast_visualizer.py                # Graphviz AST -> PNG
├── requirements.txt
├── test_arduino.txt                 # Default sample
├── test.txt                         # Older sample (outdated)
├── samples/
│   ├── blink.txt                    # LED blink
│   ├── serial_hello.txt             # Serial output
│   └── panic_test.txt               # Division-by-zero panic
├── frontend/
│   ├── ArArduinoLexer.g4            # Lexer grammar
│   ├── ArArduinoParser.g4           # Parser grammar
│   ├── ArArduinoLexer.py            # Generated lexer
│   ├── ArArduinoParser.py           # Generated parser
│   ├── ArArduinoParserVisitor.py
│   ├── ArArduinoParserListener.py
│   └── ast_builder.py               # Parse tree -> AST
├── ast_dir/
│   ├── nodes.py                     # AST node dataclasses
│   └── visitor_interface.py         # Abstract ASTVisitor
├── semantic/
│   ├── types_system.py              # Type classes
│   ├── symbols.py                   # Symbol classes
│   ├── environment.py               # Nested scopes
│   ├── builtins_registry.py         # Built-in constants and functions
│   ├── semantic_analyzer.py         # Semantic visitor + type checker
│   └── semantic_visitor.py          # Base semantic visitor
├── backend/
│   ├── ir_generator.py              # AST -> LLVM IR
│   ├── optimizer.py                 # LLVM optimization + AVR workarounds
│   ├── avr_target.py                # AVR target machine setup
│   ├── codegen.py                   # LLVM IR -> AVR assembly/object
│   ├── linker.py                    # Link + hex generation
│   └── tests/
│       └── test_backend.py          # Backend smoke tests
├── runtime/
│   └── arduino_glue.cpp             # C wrappers, main(), panic handler
├── tools/
│   ├── setup_avr_toolchain.py       # Auto-download Arduino toolchain
│   ├── build_core.py                # Build Arduino core.a
│   ├── init_antlr_alias.bat         # Windows ANTLR aliases
│   └── arduino-cli/                 # Local Arduino CLI (auto-installed)
└── docs/
    ├── PROJECT_ANALYSIS.md
    ├── PLAN.md
    ├── STEP_01.md - STEP_04.md
    └── IDE_INTEGRATION_GUIDE.md
```

---

## 6. Architecture Deep Dive

The compiler is organized as a classic multi-pass pipeline:

```text
Arabic source file
   ↓
[Normalizer]         normlize.py
   ↓
[Lexer]              ArArduinoLexer (ANTLR)
   ↓
[Parser]             ArArduinoParser (ANTLR)
   ↓
[AST Builder]        frontend/ast_builder.py
   ↓
[Semantic Analyzer]  semantic/semantic_analyzer.py
   ↓
[IR Generator]       backend/ir_generator.py
   ↓
[Optimizer]          backend/optimizer.py
   ↓
[AVR Codegen]        backend/codegen.py
   ↓
[Linker]             backend/linker.py
   ↓
[Flasher]            avrdude (via build.py)
```

Each stage produces either the input to the next stage or a diagnostic message.

### 6.1 Normalization

`normlize.py` transforms source text before parsing:

- Unicode NFC normalization
- Removes Arabic diacritics (tashkeel)
- Removes tatweel (ـ)
- Unifies hamza variants (`أ`, `إ`, `آ` → `ا`)

This means users can write `إعداد` or `اعداد` and both will match the built-in `اعداد`.

### 6.2 Lexer and Parser

The ANTLR grammars define tokens and syntax:

- `frontend/ArArduinoLexer.g4` — tokens, keywords, literals, operators
- `frontend/ArArduinoParser.g4` — grammar rules

Generated files are committed, so most developers do not need Java or ANTLR.

### 6.3 AST Builder

`ASTBuilderVisitor` walks the ANTLR parse tree and builds a custom AST using node classes from `ast_dir/nodes.py`. It also desugars operators like `+=`, `++`, and `--` into combinations of `AssignNode` and `BinOpNode`.

### 6.4 Semantic Analyzer

`SemanticAnalyzerVisitor` performs:

- Symbol table construction with nested scopes (`environment.py`)
- Type checking and inference (`types_system.py`)
- Built-in registration (`builtins_registry.py`)
- Validation of `break`/`continue` inside loops
- Function return type checking
- Error collection with line/column info

It uses `ERROR_TYPE` poisoning to avoid cascaded errors after the first failure.

### 6.5 IR Generator

`LLVMIRGenerator` translates the annotated AST into LLVM IR:

- Target triple: `avr-atmel-none`
- Pre-declares C wrapper functions: `c_pinMode`, `c_digitalWrite`, `c_delay`, etc.
- Allocates global and local variables
- Emits arithmetic, comparison, branches, and loops

### 6.6 Optimizer and AVR Backend

- `backend/optimizer.py` runs LLVM optimization passes and applies AVR-specific workarounds.
- `backend/avr_target.py` configures the ATmega328P target machine.
- `backend/codegen.py` converts optimized LLVM IR to AVR assembly or object code.
- `backend/linker.py` links `output.o` + `arduino_glue.o` + `core.a` into `firmware.hex`.

### 6.7 Runtime

`runtime/arduino_glue.cpp` provides:

- `main()` entry point
- C wrappers for Serial and GPIO
- `panic_div_zero()` runtime error handler
- Hooks to user-defined `اعداد` (setup) and `تكرار` (loop)

---

## 7. Feature Areas You Can Develop

### 7.1 Language features

| Feature | Status | Where to extend |
|---------|--------|-----------------|
| Variables and basic types | ✅ Works | `semantic/types_system.py`, `semantic/semantic_analyzer.py` |
| Functions and calls | ✅ Works | Grammar, AST, semantic, IR generator |
| Conditionals (`لو`) | ✅ Works | Grammar, AST, semantic, IR generator |
| Loops (`طالما`) | ✅ Works | Grammar, AST, semantic, IR generator |
| `ارجع` / `اقطع` / `استمر` | ✅ Works | Grammar, AST, semantic, IR generator |
| Arduino I/O | ✅ Works | `semantic/builtins_registry.py`, `runtime/arduino_glue.cpp`, `backend/ir_generator.py` |
| Serial library | ✅ Works | `semantic/builtins_registry.py`, `runtime/arduino_glue.cpp` |
| Arrays | ❌ Not implemented | Grammar, AST, semantic, IR generator, runtime |
| Structs / records | ❌ Not implemented | Grammar, AST, semantic, IR generator |
| User-defined types | ❌ Not implemented | `semantic/types_system.py`, semantic analyzer |
| Imports | ⚠️ Parsed only | `frontend/ast_builder.py`, `semantic/semantic_analyzer.py` |
| Function argument checking | ⚠️ Partial | `semantic/semantic_analyzer.py` |

### 7.2 Backend / code generation

`backend/ir_generator.py` is the main codegen file. Areas for extension:

- Complete any incomplete visitor methods.
- Add code generation for arrays, structs, strings, and chars.
- Improve `return`, `break`, and `continue` handling.
- Add more LLVM optimization passes.
- Support additional AVR chips (Mega, Nano, etc.).
- Generate debug line information.

### 7.3 Built-in functions and constants

To add a new built-in:

1. Register the normalized Arabic name in `semantic/builtins_registry.py`.
2. Generate the LLVM declaration/call in `backend/ir_generator.py`.
3. Add the C wrapper in `runtime/arduino_glue.cpp` if needed.
4. Test with a sample program.

Example: Adding a tone generator.

```python
# builtins_registry.py
register_function("نغمة", [INT_TYPE, INT_TYPE], VOID_TYPE)
```

```cpp
// arduino_glue.cpp
extern "C" void c_tone(int pin, int frequency) {
    tone(pin, frequency);
}
```

```python
# ir_generator.py — emit call to c_tone with normalized name
```

### 7.4 Normalization

`normlize.py` can be extended to:

- Normalize more Arabic spelling variants.
- Support mixed Arabic/English identifiers.
- Provide a public API for the IDE.
- Add transliteration utilities.

### 7.5 Diagnostics and error messages

The compiler currently prints errors. You can improve this by:

- Adding structured error objects with severity, stage, and source ranges.
- Adding warning levels.
- Adding friendly Arabic explanations.
- Adding an AI mentor layer.
- Emitting JSON for IDE consumption.

### 7.6 CLI and tooling

`main.py` is currently hardcoded to `test_arduino.txt`. Improvements:

- Add a proper CLI: `python main.py <source.ar> [options]`.
- Add flags: `--output`, `--stage`, `--opt-level`, `--target`, `--no-link`.
- Create a reusable `compiler_api.py` module.
- Add a JSON-RPC server or LSP implementation for IDE integration.

### 7.7 Tests

Currently only backend smoke tests exist. Add:

- Lexer/parser tests for every sample.
- Semantic analysis tests for type errors.
- IR generation golden tests.
- End-to-end tests that compile each sample to `firmware.hex`.
- Hardware-in-the-loop tests (with a connected board).

### 7.8 IDE integration

`docs/IDE_INTEGRATION_GUIDE.md` describes the expected interface. Work here includes:

- Implementing `compiler_api.py` with per-stage functions.
- Returning tokens, AST, IR, and diagnostics as structured data.
- Adding a serial monitor bridge.
- Adding board/port enumeration helpers.

---

## 8. Step-by-Step Development Workflows

### 8.1 Add a new keyword or operator

1. Update `frontend/ArArduinoLexer.g4`.
2. Update `frontend/ArArduinoParser.g4`.
3. Regenerate ANTLR files.
4. Update `frontend/ast_builder.py`.
5. Update `ast_dir/nodes.py` and `ast_dir/visitor_interface.py` if a new node is needed.
6. Implement visitors in `semantic/semantic_analyzer.py` and `backend/ir_generator.py`.
7. Add a sample and test.

### 8.2 Add a new AST node

1. Define the dataclass in `ast_dir/nodes.py`.
2. Add an abstract `visit_*` method in `ast_dir/visitor_interface.py`.
3. Build the node in `frontend/ast_builder.py`.
4. Implement the visitor in:
   - `semantic/semantic_analyzer.py`
   - `backend/ir_generator.py`
   - `ast_visualizer.py`

### 8.3 Add a new built-in function

1. `semantic/builtins_registry.py` — register the function with normalized Arabic name.
2. `backend/ir_generator.py` — declare and call the wrapper.
3. `runtime/arduino_glue.cpp` — implement the C wrapper.
4. Test with `python main.py`.

### 8.4 Regenerate ANTLR files

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener \
    frontend/ArArduinoLexer.g4 frontend/ArArduinoParser.g4
```

### 8.5 Debug LLVM IR

The compiler writes `debug.ll` to the project root. Inspect or optimize it:

```bash
python -m backend.optimizer debug.ll 2 1
```

### 8.6 Test on hardware

```bash
cp samples/blink.txt test_arduino.txt
python build.py compile
python build.py flash COM3
```

The onboard LED should blink once per second.

---

## 9. Language Reference

### 9.1 Built-in types

| Arabic | English equivalent | LLVM type |
|--------|-------------------|-----------|
| `صحيح` | integer | i32 (truncated in wrappers) |
| `عشري` | float | float |
| `نص` | string | i8* |
| `حرف` | char | i8 |
| `منطقي` | boolean | i1 |
| `فارغ` | void | void |

### 9.2 Built-in constants

| Arabic | Meaning |
|--------|---------|
| `عالي` | HIGH |
| `منخفض` | LOW |
| `مدخل` | INPUT |
| `مخرج` | OUTPUT |

### 9.3 Built-in functions

| Arabic | Arduino equivalent |
|--------|-------------------|
| `وضع_الطرف(pin, mode)` | pinMode |
| `اكتب_رقمي(pin, value)` | digitalWrite |
| `اقرا_رقمي(pin)` | digitalRead |
| `اكتب_تناظري(pin, value)` | analogWrite |
| `اقرا_تناظري(pin)` | analogRead |
| `انتظر(ms)` | delay |
| `الزمن_الحالي()` | millis |
| `سيريال_ابدا(baud)` | Serial.begin |
| `سيريال_اطبع(value)` | Serial.print |

### 9.4 Entry points

Every program must define:

```arabic
دالة اعداد():فارغ { ... }
دالة تكرار():فارغ { ... }
```

These map to Arduino's `setup()` and `loop()`.

---

## 10. Code Style and Conventions

- Language keywords and built-ins are **Arabic**; code identifiers are **English**.
- Always use **normalized Arabic** (ا only, no أ/إ/آ) in:
  - `semantic/builtins_registry.py`
  - `backend/ir_generator.py`
  - Test source files
- All AST visitors inherit from `ast_dir.visitor_interface.ASTVisitor`.
- Nodes carry `line`, `column`, and `resolved_type` metadata.
- Use `ERROR_TYPE` poisoning to avoid cascaded semantic errors.
- On Windows, set `PYTHONIOENCODING=utf-8` or use `build.py`.
- Keep functions small and focused on one compiler stage.

---

## 11. Testing Strategy

| Test type | Command | Notes |
|-----------|---------|-------|
| Backend smoke tests | `python build.py test` | Verifies IR → opt → AVR object pipeline. |
| Full compile | `python build.py compile` | Builds `output.o` and `firmware.hex`. |
| Sample blink | Compile `samples/blink.txt` and flash. | Blinks onboard LED. |
| Sample serial | Compile `samples/serial_hello.txt` and flash. | Prints via Serial Monitor. |
| Parser/semantic tests | Add `unittest` cases | Not yet implemented. |
| Hardware-in-the-loop | Flash and observe board behavior | Requires Arduino. |

### 11.1 Writing a backend test

See `backend/tests/test_backend.py` for examples. New tests should:

- Use `unittest`.
- Not depend on physical hardware.
- Assert that artifacts are produced or that specific behavior occurs.

---

## 12. Troubleshooting

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| `No module named 'llvmlite'` | venv not active | Use `.venv/Scripts/python` or activate venv |
| `Unable to find target for this triple` | llvmlite without AVR | Reinstall or build llvmlite with AVR support |
| `avr-g++ not found` | Toolchain missing | Run `python build.py setup` |
| `undefined reference to c_pinMode` | `arduino_glue.cpp` not linked | Ensure `arduino_glue.o` is in link command |
| `undefined reference to setup`/`loop` | Missing `اعداد`/`تكرار` | Add both entry points to source |
| `avrdude: stk500_getsync()` | Wrong port or baud | Check port; try `-b 57600` for old Nano |
| Arabic output is garbled | Encoding issue | Set `PYTHONIOENCODING=utf-8` |
| Program freezes | Division by zero panic | Check divisions and add guards |
| Board not detected | Driver issue | Install CH340/CP210x driver for clone boards |

---

## 13. Performance and Best Practices

- Use `build.py` to avoid manual PYTHONIOENCODING issues.
- Run slow stages (link, flash) only when needed.
- Use `python -m backend.optimizer debug.ll` to iterate on IR without recompiling source.
- Keep ANTLR regeneration rare; commit generated files.
- Profile semantic analysis on large files if adding expensive checks.
- Cache normalized text if parsing the same file multiple times.

---

## 14. Security and Safety Notes

- The compiler reads local files and writes object/hex files. Do not expose it to untrusted network input.
- Arabic normalization silently changes identifier spellings. This is intentional but must be consistent across the compiler.
- The divide-by-zero guard relies on `panic_div_zero()` in the runtime.
- When flashing hardware, verify the selected port to avoid affecting other devices.
- Do not hardcode API keys, cloud credentials, or absolute paths.

---

## 15. FAQ

**Q: Can I compile a file other than `test_arduino.txt`?**
A: Currently `main.py` is hardcoded. Copy your file to `test_arduino.txt` or modify `main.py` temporarily.

**Q: Why are built-in names normalized?**
A: So users can write `إعداد`, `اعداد`, or `أعداد` and all match the same built-in.

**Q: Can I use English identifiers in source code?**
A: The grammar supports mixed identifiers, but Arabic keywords and built-ins are expected.

**Q: Does the compiler support arrays?**
A: Not yet. Arrays are a planned feature.

**Q: Can I target boards other than Arduino Uno?**
A: The backend targets ATmega328P. Extending to other AVR chips requires changes in `backend/avr_target.py` and the linker.

**Q: How does the IDE use the compiler?**
A: The IDE shells out to the compiler via `ProModeCompilerAdapter`. See `docs/IDE_INTEGRATION_GUIDE.md`.

---

## 16. References and Next Steps

### Compiler code and architecture

- `ArduinoArabicCompiler/AGENTS.md` — AI agent instructions and file responsibilities.
- `ArduinoArabicCompiler/docs/PROJECT_ANALYSIS.md` — detailed architecture.
- `ArduinoArabicCompiler/docs/PLAN.md` — phase plan and status matrix.
- `ArduinoArabicCompiler/docs/STEP_01.md` — step 1 setup guide.
- `ArduinoArabicCompiler/docs/STEP_02.md` — step 2 setup guide.
- `ArduinoArabicCompiler/docs/STEP_03.md` — step 3 setup guide.
- `ArduinoArabicCompiler/docs/STEP_04.md` — AVR toolchain setup and flashing.
- `ArduinoArabicCompiler/docs/IDE_INTEGRATION_GUIDE.md` — IDE integration contract.
- `frontend/ArArduinoParser.g4` — canonical language syntax.
- `semantic/builtins_registry.py` — canonical list of built-ins.

### Additional guide documents in `guide_docs/`

The `ArduinoArabicCompiler/guide_docs/` directory also contains these resources:

- `كتيب_تعليمات_مترجم_الاردوينو_العربي.pdf` — Arabic instruction booklet for end users.
- `مترجم الاردوينو العربي A4.pdf` — A4-format reference/overview document.
- `ArArduino_HelpGuide.html` — HTML help guide for the Arabic Arduino language.
- `ArArduino_Presentation.pptx` — Introductory presentation slides.

---

## Quick Checklist for New Contributors

- [ ] Virtual environment created and dependencies installed.
- [ ] `python build.py test` passes.
- [ ] `python build.py compile` produces `output.o` and `firmware.hex`.
- [ ] You understand which pipeline stage you want to change.
- [ ] If modifying built-ins, you used normalized Arabic names.
- [ ] If adding AST nodes, you updated all visitors.
- [ ] You tested on a sample before committing.

Happy compiling! ⚙️
