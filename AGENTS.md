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
├── normlize.py                 # Arabic text normalization pipeline
├── ast_visualizer.py           # Graphviz AST -> PNG visitor
├── requirements.txt            # Python dependencies
├── test_arduino.txt            # Current working sample program
├── test.txt                    # Older sample; uses outdated built-in names
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
│   └── semantic_analyzer.py    # Semantic visitor + type checker
├── backend/
│   ├── ir_generator.py         # AST -> LLVM IR generator
│   └── optimizer.py            # LLVM IR optimization + AVR object/assembly emission
└── tools/
    └── init_antlr_alias.bat    # Windows doskey aliases for antlr4 / grun
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
  It pre-declares C wrapper functions (`c_pinMode`, `c_digitalWrite`, ...).
- `Optimizer` parses the IR, runs LLVM optimization passes, applies an AVR
  workaround for unsigned-less-than comparisons with large constants, and can
  emit AVR assembly or a `.o` file.

## Build and run commands

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\pip install -r requirements.txt
# Linux/macOS:
# .venv/bin/pip install -r requirements.txt
```

Run the compiler on the default sample:

```bash
# Windows terminal default encoding is cp1252; force UTF-8 to avoid
# UnicodeEncodeError when printing Arabic messages.
set PYTHONIOENCODING=utf-8
.venv\Scripts\python main.py
```

Successful output prints Arabic semantic-analysis messages, the generated LLVM
IR, AVR assembly, and writes `output.o`.

### Stand-alone optimizer

```bash
.venv\Scripts\python -m backend.optimizer input.ll [opt_level] [size_level]
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

There is **no automated test suite** in the repository at the moment.
Verification is currently manual:

- Run `python main.py` and inspect the semantic-analysis output, LLVM IR, and
  AVR assembly.
- Modify `test_arduino.txt` to exercise language features.
- Use `backend/optimizer.py` standalone to validate generated IR.

Samples:

- `test_arduino.txt` — current, working example (LED fade using `اعداد`,
  `تكرار`, `وضع_الطرف`, `اكتب_تناظري`, `انتظر`).
- `test.txt` — older example that uses built-in names not registered in the
  current symbol table (`كتابة_تناظرية`, `تأخير`), so it fails semantic analysis.

`.gitignore` references a future `test_ai_nodes.py`, but that file is not
present.

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

## Known limitations and risks

- `main.py` is hard-coded to `test_arduino.txt`.
- The semantic analyzer does **not** validate function-call arity or argument
  types; it only checks that the name is defined.
- `import` statements are parsed but have no semantic effect except that the
  Serial library symbols are pre-declared.
- Some built-in names are not normalized consistently between the semantic
  registry and the IR generator. For example, the registry uses `اقرا_رقمي`
  while `ir_generator.py` uses `اقرأ_رقمي`; after source normalization a
  lookup may fail. Use normalized (`ا` only) keys everywhere when adding or
  changing built-ins.
- `test.txt` is out of date and will produce semantic errors.
- The AVR backend is only available if the installed `llvmlite` binary was
  built with AVR support. `Optimizer` falls back to the host target for
  optimization-only runs, but `emit_assembly` / `emit_object` require AVR.
- Advanced features (arrays, structs, user-defined types, full import/linking)
  are not implemented.

## Useful references

- `PROJECT_ANALYSIS.md` — more detailed architecture description and a file-map
  by responsibility.
- `frontend/ArArduinoParser.g4` and `frontend/ArArduinoLexer.g4` — the language
  syntax.
- `semantic/builtins_registry.py` — canonical list of constants, functions, and
  hardware registers.
- `backend/optimizer.py` — AVR-specific LLVM optimization details and the
  `icmp ult` workaround.
