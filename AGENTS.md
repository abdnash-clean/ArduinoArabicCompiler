# AGENTS.md — Arduino Arabic Compiler

> This file did not exist before this exploration. It was created from the actual
> project contents to give AI coding agents a reliable, project-specific
> starting point.

## Project overview

This repository implements an **Arabic-inspired compiler front-end for
Arduino-style programs**. It is written in Python and transforms Arabic source
code into LLVM IR, optionally optimizes it for AVR (ATmega328P / Arduino Uno),
and can emit AVR assembly or a `.o` object file.

The language keywords, built-in names, and most user-facing identifiers are in
**Arabic**. The compiler pipeline is:

1. Read the source file (`test_arduino.txt` by default).
2. Normalize Arabic text (NFC, remove tashkeel/tatweel, unify hamza forms).
3. Lex and parse with ANTLR4-generated `ArArduinoLexer` / `ArArduinoParser`.
4. Build an AST with `frontend/ast_builder.py`.
5. Run semantic analysis (scope, type checking, built-in symbols) with
   `semantic/semantic_analyzer.py`.
6. If no errors, generate LLVM IR with `backend/ir_generator.py`.
7. Optimize the IR and emit AVR assembly / object code with `backend/optimizer.py`.

## Technology stack

- **Language:** Python 3 (tested on Python 3.14; wheels for `llvmlite` may limit
  the exact version on some platforms).
- **Parser generator:** ANTLR 4.13.2.
- **LLVM bindings:** llvmlite 0.47.0.
- **Optional visualization:** graphviz (used by `ast_visualizer.py`).

Dependencies are listed in `requirements.txt`:

```text
antlr4-python3-runtime==4.13.2
llvmlite==0.47.0
```

## Repository layout

```text
.
├── main.py                     # Compiler driver (hardcodes test_arduino.txt)
├── build.py                    # Build helper (compile, link, flash, test)
├── normlize.py                 # Arabic text normalization pipeline
├── ast_visualizer.py           # Graphviz AST -> PNG visitor
├── requirements.txt            # Python dependencies
├── test_arduino.txt            # Current working sample: autonomous robot controller
├── test.txt                    # Older sample; uses outdated built-in names
├── AGENTS.md                   # AI agent instructions and conventions
├── PROJECT_ANALYSIS.md         # Detailed human-readable analysis
├── frontend/
│   ├── ArArduinoLexer.g4       # ANTLR lexer grammar
│   ├── ArArduinoParser.g4      # ANTLR parser grammar
│   ├── ArArduinoLexer.py       # Generated lexer
│   ├── ArArduinoParser.py      # Generated parser
│   ├── ArArduinoParserVisitor.py
│   ├── ArArduinoParserListener.py
│   └── ast_builder.py          # Parse tree -> AST visitor
├── ast_dir/
│   ├── nodes.py                # AST node dataclasses
│   └── visitor_interface.py    # Abstract ASTVisitor base class
├── semantic/
│   ├── types_system.py         # Type classes (Int, Float, String, Bool, Void, Error)
│   ├── symbols.py              # Symbol / VariableSymbol / FunctionSymbol / ConstantSymbol
│   ├── environment.py          # Nested scope environment
│   ├── builtins_registry.py    # Arduino constants, functions, registers, Serial lib
│   ├── semantic_analyzer.py    # Semantic visitor + type checker
│   └── semantic_visitor.py     # Base semantic visitor
├── backend/
│   ├── ir_generator.py         # AST -> LLVM IR generator
│   ├── optimizer.py            # LLVM IR optimization + AVR object/assembly emission
│   ├── avr_target.py           # AVR (ATmega328P) target machine setup
│   ├── codegen.py              # LLVM IR -> AVR assembly/object code
│   ├── linker.py               # Object linking + hex generation
│   └── tests/
│       └── test_backend.py     # Smoke tests for backend pipeline
├── runtime/
│   └── arduino_glue.cpp        # C wrappers, main(), panic handler, Serial/GPIO functions
├── samples/
│   ├── blink.txt               # LED blink example (simplest)
│   ├── serial_hello.txt        # Serial communication example
│   └── panic_test.txt          # Division by zero panic handler test
├── docs/
│   ├── PLAN.md                 # Phase plan and status matrix
│   ├── PROJECT_ANALYSIS.md     # Detailed architecture
│   ├── STEP_01.md - STEP_04.md # Step-by-step setup guides
│   └── IDE_INTEGRATION_GUIDE.md
└── tools/
    ├── setup_avr_toolchain.py  # Auto-download & install Arduino toolchain
    ├── build_core.py           # Build Arduino core.a library
    ├── init_antlr_alias.bat    # Windows doskey aliases
    └── arduino-cli/            # Local Arduino CLI and toolchain (auto-installed)
```

## Runtime architecture / data flow

- `main.py` orchestrates the whole pipeline. It currently reads
  `test_arduino.txt` from the working directory.
- `normalize_arabic_text()` in `normlize.py` removes diacritics, tatweel, and
  normalizes `أ`, `إ`, `آ` to `ا`. This normalization affects identifier
  matching, including built-in names.
- `ASTBuilderVisitor` (`frontend/ast_builder.py`) desugars `+=`, `-=`, `++`,
  `--` into `AssignNode` + `BinOpNode` combinations.
- `SemanticAnalyzerVisitor` collects errors in `self.errors` and annotates
  `node.resolved_type`. It allows implicit `صحيح` -> `عشري` widening.
- `LLVMIRGenerator` emits LLVM IR targeting the triple `avr-atmel-none`.
  It pre-declares C wrapper functions (`c_pinMode`, `c_digitalWrite`, `c_serialPrintInt`, `c_serialPrintFloat`, `c_serialPrintString`).
- **Modular backend:**
  - `avr_target.py`: Sets up `TargetMachine` for AVR (ATmega328P).
  - `codegen.py`: Converts LLVM IR to AVR assembly or object files.
  - `optimizer.py`: Runs LLVM optimization passes and applies AVR-specific workarounds (e.g., `icmp ult` with large constants).
  - `linker.py`: Links `output.o` + `runtime/arduino_glue.cpp` (compiled to `.o`) + `core.a` to produce `firmware.hex` via `avr-objcopy`.
- `runtime/arduino_glue.cpp`: Provides `main()`, C wrappers for Serial/GPIO, `panic_div_zero()`, and hooks to user-defined `اعداد()` / `setup()` and `تكرار()` / `loop()`.

## Build and run commands

### Initial setup

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\pip install -r requirements.txt
# Linux/macOS:
# .venv/bin/pip install -r requirements.txt
```

### Quick build workflow (recommended)

Use the provided `build.py` helper for common tasks:

```bash
# One-time setup: install Arduino AVR toolchain and build core.a
python build.py setup

# Compile: main.py → output.o (and temporary LLVM IR)
python build.py compile

# Run backend tests
python build.py test

# Link: output.o + core.a → firmware.hex
python build.py link

# Flash to Arduino Uno (auto-detects port or use --port COM5)
python build.py flash
python build.py flash --port COM5

# Clean all generated files
python build.py clean
```

**Windows note:** The build system forces `PYTHONIOENCODING=utf-8` automatically
to avoid UnicodeEncodeError when printing Arabic messages.

See [STEP_04.md](docs/STEP_04.md) for detailed setup and troubleshooting.

### Manual compilation workflow

If not using `build.py`:

```bash
set PYTHONIOENCODING=utf-8
python main.py
```

This runs the full pipeline: lex → parse → AST → semantic analysis → LLVM IR → optimization → AVR assembly + `output.o`.

### Stand-alone optimizer

```bash
python -m backend.optimizer input.ll [opt_level] [size_level]
```

Recommended for AVR: `opt_level=2`, `size_level=1` (equivalent to `-Os`).

### Regenerating ANTLR files

The generated files are committed, so a normal build does not need Java or
ANTLR. To regenerate from the `.g4` grammars:

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener \
    frontend/ArArduinoLexer.g4 frontend/ArArduinoParser.g4
```

`tools/init_antlr_alias.bat` sets up Windows `doskey` aliases for `antlr4` and
`grun`, but it hardcodes an absolute path to the ANTLR jar on the original
machine.

## Testing strategy

**Automated backend tests** verify the IR generation → optimization → AVR codegen pipeline:

```bash
python build.py test  # or: python -m unittest backend.tests.test_backend -v
```

These smoke tests check:
- AVR target registration and `TargetMachine` creation
- LLVM IR optimization and AVR object file emission
- Arduino glue layer compilation (if AVR toolchain available)
- Serial function overload selection

**Sample programs** demonstrate language features:

| Sample | Purpose | Features used |
|--------|---------|---------------|
| `samples/blink.txt` | Simplest: LED blink on pin 13 | `وضع_الطرف`, `اكتب_رقمي`, `انتظر`, `اعداد`, `تكرار` |
| `samples/serial_hello.txt` | Serial output example | `استيراد "سيريال"`, `سيريال_ابدا`, `سيريال_اطبع`, variable increment |
| `samples/panic_test.txt` | Division by zero panic | Tests `panic_div_zero()` runtime handler |
| `test_arduino.txt` | Complex: autonomous robot | Motors, analog I/O, conditionals, variables, loop logic |

**Manual verification:**

```bash
python main.py                           # Compile test_arduino.txt
python -m backend.optimizer debug.ll 2 1 # Standalone IR optimization
python build.py flash COM5               # Upload to Arduino Uno
```

Note: `test.txt` is outdated and uses incorrect built-in names; it will fail semantic analysis.

## Code style and conventions

- **Identifiers:** Language keywords and built-ins are Arabic. Code uses a mix
  of Arabic comments and English identifiers where required by the tooling
  (e.g., ANTLR visitor method names).
- **AST visitor pattern:** All AST passes inherit from `ast_dir.visitor_interface.ASTVisitor`
  and implement `visit_<NodeName>` methods.
- **Node metadata:** AST nodes are dataclasses with `line`, `column`, and
  `resolved_type` fields. `set_metadata()` in `ASTBuilderVisitor` copies source
  locations from ANTLR contexts.
- **Type mapping:** String keywords such as `صحيح`, `عشري`, `نص`, `منطقي`,
  `فارغ` are mapped to singleton type objects in `semantic/types_system.py`.
- **Error handling:** Semantic analysis uses `ERROR_TYPE` poisoning to avoid
  cascaded errors after the first failure.
- **Module imports:** Several modules use `from ast_dir.nodes import *`; when
  adding new node types, keep `nodes.py` and `visitor_interface.py` in sync and
  update all visitors (`semantic_analyzer.py`, `ir_generator.py`,
  `ast_visualizer.py`).
- **Built-in function normalization:** The register and IR generator must use
  **normalized Arabic only** (أ/إ/آ → ا). Example: `اقرا_رقمي` (not `اقرأ_رقمي`
  with hamza). See [semantic/builtins_registry.py](semantic/builtins_registry.py).
- **Serial functions (post-Phase 3):** `Serial.print()` is no longer variadic.
  Use `c_serialPrintInt()`, `c_serialPrintFloat()`, `c_serialPrintString()`
  instead to maintain type safety and avoid complex ABI issues on AVR.
- **Type widening:** Implicit `صحيح` (32-bit) → `عشري` (32-bit float) is allowed.
  All types are 32-bit in LLVM; AVR C wrappers must handle truncation to 16-bit `int` where needed.

## Security considerations

- The compiler reads a local file and writes `output.o` (and potentially PNG
  files if the AST visualizer is enabled). It does not sandbox the source code;
  a malformed input can raise exceptions or produce invalid IR.
- Arabic normalization can silently change identifier spellings
  (`أ`/`إ`/`آ` -> `ا`). This is intentional for user source code, but it means
  built-in names in `semantic/builtins_registry.py`, `backend/ir_generator.py`,
  and source code must be kept consistent after normalization.
- The divide-by-zero guard in `ir_generator.py` emits a call to an external
  `panic_div_zero()` symbol; the runtime must provide this symbol.
- Do not expose the compiler to untrusted network input without additional
  hardening.

## Project status

✅ **Fully functional and tested on hardware:**

- [x] Lexer/parser with full Arabic grammar (binary/hex/octal literals, operators, control flow)
- [x] Complete semantic analysis with symbol table and type checking
- [x] LLVM IR generation with Arduino built-in function mapping
- [x] AVR optimization (O2, Os) with `icmp ult` workaround
- [x] Linker: `output.o` + `arduino_glue.o` + `core.a` → `firmware.hex`
- [x] Auto-install AVR toolchain via `python build.py setup`
- [x] Flash to Arduino Uno: `python build.py flash COM5`
- [x] Backend smoke tests in `backend/tests/test_backend.py`
- [x] Verified samples: `blink.txt`, `serial_hello.txt`, `panic_test.txt`
- [x] Complex real-world example: `test_arduino.txt` (autonomous robot with motors/sensors)

**Last hardware verification:** `python build.py flash COM5` ✅ (exit 0)

## Known limitations and risks

- `main.py` is hard-coded to `test_arduino.txt`. To compile a different source file, temporarily edit `main.py` or use a symlink/rename.
- The semantic analyzer does **not** validate function-call arity or argument
  types; it only checks that the name is defined. Full argument type checking is a future enhancement.
- `import` statements are parsed but have no semantic effect except that the
  Serial library symbols are pre-declared.
- Some built-in names may not be normalized consistently between the semantic
  registry and the IR generator. **Always use normalized Arabic** (ا only, no أ/إ/آ) in `semantic/builtins_registry.py`, `ir_generator.py`, and test files.
- `test.txt` is out of date and will produce semantic errors.
- The AVR backend requires `llvmlite` built with AVR support. Check with:
  ```bash
  python -c "import llvmlite.binding as llvm; print(llvm.Target.from_triple('avr-atmel-none'))"
  ```
  If this fails, your `llvmlite` wheel doesn't include AVR.
- Advanced features (arrays, structs, user-defined types, full import/linking)
  are not implemented.

## Common development patterns and troubleshooting

### Running the full pipeline

```bash
python build.py setup    # One-time: install toolchain and build core.a
python build.py compile   # Compile source to IR and object file
python build.py test       # Run backend tests
python build.py link       # Link object + core -> firmware.hex
python build.py flash      # Upload firmware to Arduino
```

### Adding a new built-in constant or function

1. Register in [semantic/builtins_registry.py](semantic/builtins_registry.py) with **normalized Arabic only**.
2. Generate LLVM IR for it in [backend/ir_generator.py](backend/ir_generator.py) (use same normalized name).
3. If it calls a C wrapper, add the wrapper to [runtime/arduino_glue.cpp](runtime/arduino_glue.cpp).
4. Test with a sample in `test_arduino.txt` and run `python main.py`.

### Debugging semantic errors

Run the compiler and check the error output:
```bash
set PYTHONIOENCODING=utf-8
python main.py 2>&1 | more
```

Errors are printed in Arabic with line/column info. Use [semantic/semantic_analyzer.py](semantic/semantic_analyzer.py) to add more validation.

### Debugging LLVM IR

The compiler writes temporary `debug.ll` to the project root. Inspect it:
```bash
python -m backend.optimizer debug.ll 2 1    # Optimize with -O2 -Os
```

### AVR toolchain not found

If `python build.py flash` fails with "avrdude not found", run setup:
```bash
python build.py setup
```

This downloads and builds the AVR toolchain inside `tools/arduino-cli/`.

### PYTHONIOENCODING errors on Windows

Ensure `PYTHONIOENCODING=utf-8` is set before running any Python command:
```bash
set PYTHONIOENCODING=utf-8
python main.py
```

Or use `build.py` which sets it automatically.

## Useful references

- [docs/PROJECT_ANALYSIS.md](docs/PROJECT_ANALYSIS.md) — detailed architecture description and file-map by responsibility.
- [frontend/ArArduinoParser.g4](frontend/ArArduinoParser.g4) and [frontend/ArArduinoLexer.g4](frontend/ArArduinoLexer.g4) — the language syntax.
- [semantic/builtins_registry.py](semantic/builtins_registry.py) — canonical list of constants, functions, and hardware registers.
- [backend/optimizer.py](backend/optimizer.py) — AVR-specific LLVM optimization details and the `icmp ult` workaround.
- [docs/STEP_04.md](docs/STEP_04.md) — setup and troubleshooting guide for AVR toolchain and flashing.

## Module and file responsibilities

When adding features or fixing bugs, consult this guide:

| File | Responsibility | When to edit |
|------|---|---|
| [main.py](main.py) | Orchestrates the entire pipeline | Rarely; changing input source file |
| [normlize.py](normlize.py) | Arabic text normalization (remove diacritics, etc.) | Fixing normalization bugs; adding new forms |
| [frontend/ArArduinoLexer.g4](frontend/ArArduinoLexer.g4) | Token definitions | Adding new keywords or operators |
| [frontend/ArArduinoParser.g4](frontend/ArArduinoParser.g4) | Grammar rules | Changing language syntax |
| [frontend/ast_builder.py](frontend/ast_builder.py) | Parse tree → AST | Desugaring new syntactic constructs; fixing AST structure |
| [ast_dir/nodes.py](ast_dir/nodes.py) | AST node definitions | Adding new node types (then update all visitors) |
| [semantic/types_system.py](semantic/types_system.py) | Type classes and operations | Adding new types or type operations |
| [semantic/builtins_registry.py](semantic/builtins_registry.py) | Built-in constants/functions | Adding/updating Arduino functions and I/O ports |
| [semantic/semantic_analyzer.py](semantic/semantic_analyzer.py) | Semantic analysis, scope, and type checking | Adding validation rules; fixing type errors |
| [backend/ir_generator.py](backend/ir_generator.py) | AST → LLVM IR | Adding code generation for new nodes/features |
| [backend/avr_target.py](backend/avr_target.py) | AVR target machine setup | Rare; tuning AVR target configuration |
| [backend/codegen.py](backend/codegen.py) | LLVM IR → AVR assembly / object | Rare; architecture-specific assembly tweaks |
| [backend/optimizer.py](backend/optimizer.py) | LLVM IR optimization + AVR workarounds | Fixing optimization bugs; adding AVR-specific passes |
| [backend/linker.py](backend/linker.py) | Linking + hex generation | Changing link workflow or firmware output |
| [runtime/arduino_glue.cpp](runtime/arduino_glue.cpp) | C wrappers, main(), panic handler | Adding C wrappers for new builtins; changing entry point |
| [semantic/environment.py](semantic/environment.py) | Symbol table / scoping | Rarely; scoping semantics |
| [semantic/symbols.py](semantic/symbols.py) | Symbol classes (Variable, Function, etc.) | Adding new symbol metadata |
