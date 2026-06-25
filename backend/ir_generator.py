# backend/ir_generator.py
from llvmlite import ir
from ast_dir.visitor_interface import ASTVisitor
from ast_dir.nodes import *
from semantic.types_system import *
from semantic.builtins_registry import REGISTERS


class LLVMIRGenerator(ASTVisitor):
    def __init__(self):
        # 1. LLVM Module
        self.module = ir.Module(name="ar_arduino_module")
        self.module.triple = "avr-atmel-none"

        # 2. Builder (None while we are in global scope)
        self.builder = None

        # 3. Environments / stacks
        self.llvm_env = {}      # variable name -> memory pointer
        self.loop_stack = []    # (cond_block, end_block) for break/continue
        self.functions = {}     # arabic function name -> ir.Function (user defined)
        self.builtins = {}      # arabic builtin name  -> ir.Function (C wrappers)
        self.string_counter = 0 # unique names for string literals

        # 4. LLVM primitive types
        self.i32 = ir.IntType(32)        # صحيح
        self.f64 = ir.DoubleType()       # عشري
        self.i1 = ir.IntType(1)          # منطقي
        self.i8 = ir.IntType(8)          # حرف
        self.void = ir.VoidType()        # فارغ
        self.i8_ptr = ir.IntType(8).as_pointer()  # نص

        # 5. Pre-declare Arduino built-in external functions
        self._declare_builtins()

        # 6. Pre-create volatile pointers for hardware registers
        self.registers = {}
        self._declare_registers()

    # ==========================================
    # Helpers
    # ==========================================
    def _get_llvm_type(self, semantic_type):
        """Map a semantic Type object to an LLVM type."""
        if semantic_type == INT_TYPE: return self.i32
        if semantic_type == FLOAT_TYPE: return self.f64
        if semantic_type == BOOL_TYPE: return self.i1
        if semantic_type == STRING_TYPE: return self.i8_ptr
        return self.void

    def _get_llvm_type_from_string(self, type_str: str):
        """Map an Arabic type keyword from the AST to an LLVM type."""
        mapping = {
            'صحيح': self.i32,
            'رقم': self.i32,
            'عشري': self.f64,
            'كسري': self.f64,
            'نص': self.i8_ptr,
            'منطقي': self.i1,
            'حرف': self.i8,
            'فارغ': self.void,
        }
        return mapping.get(type_str, self.void)

    def _declare_builtins(self):
        """Declare the C/C++ wrapper functions so LLVM knows they exist."""
        def declare(name, ret, params, var_arg=False):
            ft = ir.FunctionType(ret, params, var_arg=var_arg)
            return ir.Function(self.module, ft, name=name)

        # Core Arduino API (mapped from the Arabic names in builtins_registry)
        self.builtins['وضع_الطرف']    = declare("c_pinMode",      self.void, [self.i32, self.i32])  # pinMode
        self.builtins['اكتب_رقمي']    = declare("c_digitalWrite", self.void, [self.i32, self.i32])  # digitalWrite
        self.builtins['اقرا_رقمي']    = declare("c_digitalRead",  self.i32,  [self.i32])            # digitalRead
        self.builtins['اكتب_تناظري']  = declare("c_analogWrite",  self.void, [self.i32, self.i32])  # analogWrite
        self.builtins['اقرا_تناظري']  = declare("c_analogRead",   self.i32,  [self.i32])            # analogRead
        self.builtins['انتظر']        = declare("c_delay",        self.void, [self.i32])            # delay
        self.builtins['الزمن_الحالي'] = declare("c_millis",       self.i32,  [])                    # millis

        # Serial library (سيريال) — declared up-front; harmless if unused
        self.builtins['سيريال_ابدا'] = declare("c_serialBegin", self.void, [self.i32])             # Serial.begin
        # Serial.print overloads — AVR glue uses typed wrappers, not variadic
        self.builtins['سيريال_اطبع_صحيح'] = declare("c_serialPrintInt",    self.void, [self.i32])    # Serial.print(int)
        self.builtins['سيريال_اطبع_عشري'] = declare("c_serialPrintFloat",  self.void, [self.f64])    # Serial.print(float)
        self.builtins['سيريال_اطبع_نص']   = declare("c_serialPrintString", self.void, [self.i8_ptr]) # Serial.print(string)

        # Keep backwards-compatible attribute names
        self.c_pinMode = self.builtins['وضع_الطرف']
        self.c_digitalWrite = self.builtins['اكتب_رقمي']
        self.c_delay = self.builtins['انتظر']

        panic_type = ir.FunctionType(self.void, [])
        self.panic_func = ir.Function(self.module, panic_type, name="panic_div_zero")

    def _declare_registers(self):
        """Map each Arabic register name to a volatile 8-bit pointer at a fixed address."""
        addr_int = ir.IntType(16)  # AVR data pointers are 16-bit
        for name, addr in REGISTERS.items():
            self.registers[name] = ir.Constant(addr_int, addr).inttoptr(self.i8_ptr)

    def get_ir(self):
        """Return the final LLVM IR as a string."""
        return str(self.module)

    def _cast_if_needed(self, val, target_llvm_type):
        """Cast i32 -> f64 (constant fold in global scope, sitofp inside a function)."""
        if val.type == self.i32 and target_llvm_type == self.f64:
            if self.builder is None:
                return ir.Constant(self.f64, float(val.constant))
            return self.builder.sitofp(val, self.f64, name="cast_to_float")
        return val

    def _cast_value(self, val, target_type):
        """Best-effort cast of a value to a target LLVM type (used for args/returns)."""
        if val is None or val.type == target_type:
            return val
        # int <-> float
        if val.type == self.i32 and target_type == self.f64:
            return self._cast_if_needed(val, self.f64)
        if val.type == self.f64 and target_type == self.i32:
            return self.builder.fptosi(val, self.i32, name="cast_to_int")
        # bool (i1) -> int
        if val.type == self.i1 and target_type == self.i32:
            return self.builder.zext(val, self.i32, name="bool_to_int")
        # int -> bool (i1)
        if val.type == self.i32 and target_type == self.i1:
            return self.builder.icmp_signed('!=', val, ir.Constant(self.i32, 0), name="int_to_bool")
        # char (i8) -> int
        if val.type == self.i8 and target_type == self.i32:
            return self.builder.sext(val, self.i32, name="char_to_int")
        return val

    def _unify_numeric(self, left, right):
        """Promote one operand to f64 if the operands are mixed int/float."""
        if left.type == self.f64 and right.type == self.i32:
            right = self._cast_if_needed(right, self.f64)
        elif left.type == self.i32 and right.type == self.f64:
            left = self._cast_if_needed(left, self.f64)
        return left, right

    def _make_global_string(self, text: str):
        """Create an internal constant string and return an i8* to its first byte."""
        encoded = bytearray(text.encode("utf-8")) + b"\x00"
        str_type = ir.ArrayType(self.i8, len(encoded))
        name = f".str.{self.string_counter}"
        self.string_counter += 1

        gvar = ir.GlobalVariable(self.module, str_type, name=name)
        gvar.linkage = "internal"
        gvar.global_constant = True
        gvar.initializer = ir.Constant(str_type, encoded)

        zero = ir.Constant(self.i32, 0)
        # Constant GEP works both at global scope and inside functions.
        return gvar.gep([zero, zero])

    # ==========================================
    # Node Visiting Methods
    # ==========================================
    def visit_ProgramNode(self, node: ProgramNode):
        # Pass 1: declare all user function prototypes (allows forward references)
        for decl in node.declarations:
            if isinstance(decl, FuncDeclNode):
                self._declare_function(decl)
        # Pass 2: emit global declarations (variables, imports, ...)
        for decl in node.declarations:
            if not isinstance(decl, FuncDeclNode):
                decl.accept(self)
        # Pass 3: emit function bodies
        for decl in node.declarations:
            if isinstance(decl, FuncDeclNode):
                decl.accept(self)

    def _declare_function(self, node: FuncDeclNode):
        """Create the LLVM Function object (signature only) and register it."""
        llvm_func_name = node.name
        if node.name == 'اعداد':
            llvm_func_name = 'setup'
        elif node.name == 'تكرار':
            llvm_func_name = 'loop'

        ret_type = self._get_llvm_type_from_string(node.return_type)
        param_types = [self._get_llvm_type_from_string(p[1]) for p in node.params]
        func_type = ir.FunctionType(ret_type, param_types)
        func = ir.Function(self.module, func_type, name=llvm_func_name)

        for i, arg in enumerate(func.args):
            arg.name = node.params[i][0]

        self.functions[node.name] = func
        return func

    def visit_VarDeclNode(self, node: VarDeclNode):
        llvm_type = self._get_llvm_type_from_string(node.var_type)

        # CASE 1: GLOBAL VARIABLE
        if self.builder is None:
            ptr = ir.GlobalVariable(self.module, llvm_type, name=node.name)
            ptr.linkage = 'internal'
            if node.value:
                val = node.value.accept(self)
                val = self._cast_if_needed(val, llvm_type)
                ptr.initializer = val
            else:
                ptr.initializer = ir.Constant(llvm_type, None)
            self.llvm_env[node.name] = ptr

        # CASE 2: LOCAL VARIABLE
        else:
            ptr = self.builder.alloca(llvm_type, name=node.name)
            self.llvm_env[node.name] = ptr
            if node.value:
                val = node.value.accept(self)
                val = self._cast_value(val, llvm_type)
                self.builder.store(val, ptr)

    def visit_AssignNode(self, node: AssignNode):
        # Hardware register write (truncate i32 -> i8, volatile store).
        if node.name in self.registers:
            val = node.value.accept(self)
            val = self._cast_value(val, self.i32)
            val8 = self.builder.trunc(val, self.i8, name="reg_trunc")
            st = self.builder.store(val8, self.registers[node.name])
            st.volatile = True
            return val

        val = node.value.accept(self)
        ptr = self.llvm_env[node.name]
        # Cast to the actual storage type of the variable.
        val = self._cast_value(val, ptr.type.pointee)
        self.builder.store(val, ptr)
        return val

    def visit_FuncDeclNode(self, node: FuncDeclNode):
        # Function object already created in pass 1.
        func = self.functions[node.name]
        ret_type = func.function_type.return_type

        block = func.append_basic_block(name="entry")

        previous_builder = self.builder
        previous_env = self.llvm_env.copy()
        self.builder = ir.IRBuilder(block)

        # Allocate stack slots for parameters and store incoming arguments.
        for i, arg in enumerate(func.args):
            arg_name = node.params[i][0]
            ptr = self.builder.alloca(arg.type, name=arg_name + "_ptr")
            self.builder.store(arg, ptr)
            self.llvm_env[arg_name] = ptr

        if node.body:
            node.body.accept(self)

        # Guarantee the entry/last block is terminated.
        if not self.builder.block.is_terminated:
            if ret_type == self.void:
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(ret_type, 0))

        self.builder = previous_builder
        self.llvm_env = previous_env

    def visit_BlockNode(self, node: BlockNode):
        for stmt in node.statements:
            stmt.accept(self)
            # Stop emitting after a terminator (return/break/continue) in this block.
            if self.builder is not None and self.builder.block.is_terminated:
                break

    def visit_FuncCallNode(self, node: FuncCallNode):
        # Special-case: Serial.print dispatches to a typed overload on AVR.
        if node.name == 'سيريال_اطبع':
            if not node.args:
                raise Exception("خطأ هندسي: استدعاء 'سيريال_اطبع' يحتاج وسيطاً واحداً على الأقل.")
            arg_val = node.args[0].accept(self)
            if arg_val.type == self.f64:
                func = self.builtins['سيريال_اطبع_عشري']
            elif arg_val.type == self.i8_ptr:
                func = self.builtins['سيريال_اطبع_نص']
            else:
                func = self.builtins['سيريال_اطبع_صحيح']
                arg_val = self._cast_value(arg_val, self.i32)
            return self.builder.call(func, [arg_val])

        arg_vals = [arg.accept(self) for arg in node.args]

        # Resolve target: built-in first, then user-defined.
        func = self.builtins.get(node.name) or self.functions.get(node.name)
        if func is None:
            raise Exception(f"خطأ هندسي: استدعاء لدالة غير معرفة '{node.name}'.")

        # Cast each argument to the declared parameter type.
        fixed_params = list(func.function_type.args)
        casted = []
        for i, val in enumerate(arg_vals):
            if i < len(fixed_params):
                casted.append(self._cast_value(val, fixed_params[i]))
            else:
                casted.append(val)

        return self.builder.call(func, casted)

    def visit_IfNode(self, node: IfNode):
        cond_val = node.condition.accept(self)
        cond_val = self._cast_value(cond_val, self.i1)
        current_function = self.builder.function
        then_bb = current_function.append_basic_block("then")
        merge_bb = current_function.append_basic_block("ifcont")
        if node.else_block:
            else_bb = current_function.append_basic_block("else")
            self.builder.cbranch(cond_val, then_bb, else_bb)
        else:
            self.builder.cbranch(cond_val, then_bb, merge_bb)

        self.builder.position_at_end(then_bb)
        node.then_block.accept(self)
        if not self.builder.block.is_terminated:
            self.builder.branch(merge_bb)

        if node.else_block:
            self.builder.position_at_end(else_bb)
            node.else_block.accept(self)
            if not self.builder.block.is_terminated:
                self.builder.branch(merge_bb)

        self.builder.position_at_end(merge_bb)

    def visit_WhileNode(self, node: WhileNode):
        current_func = self.builder.function
        cond_bb = current_func.append_basic_block("while_cond")
        body_bb = current_func.append_basic_block("while_body")
        end_bb = current_func.append_basic_block("while_end")

        self.builder.branch(cond_bb)

        self.builder.position_at_end(cond_bb)
        cond_val = node.condition.accept(self)
        if cond_val is None:
            raise Exception("خطأ هندسي: تعذر تقييم شرط الحلقة.")
        cond_val = self._cast_value(cond_val, self.i1)
        self.builder.cbranch(cond_val, body_bb, end_bb)

        self.builder.position_at_end(body_bb)
        self.loop_stack.append((cond_bb, end_bb))
        node.body.accept(self)
        self.loop_stack.pop()

        if not self.builder.block.is_terminated:
            self.builder.branch(cond_bb)

        self.builder.position_at_end(end_bb)

    def emit_runtime_trap(self, is_danger_i1):
        """Divide-by-zero guard. If is_danger_i1 is true, jump to a
        panic block that calls panic_div_zero() and halts; otherwise fall through
        to a safe 'math_block'. Leaves the builder positioned in the safe block."""
        current_func = self.builder.function
        panic_bb = current_func.append_basic_block("panic_block")
        continue_bb = current_func.append_basic_block("math_block")
        # Conditional jump: danger -> panic, else -> safe path.
        self.builder.cbranch(is_danger_i1, panic_bb, continue_bb)
        # Panic block: call the handler (defined in arduino_glue.cpp), then mark
        # the path 'unreachable' so the optimizer can reason about / delete it.
        self.builder.position_at_end(panic_bb)
        self.builder.call(self.panic_func, [])
        self.builder.unreachable()
        # Move the cursor back to the safe block to resume normal codegen.
        self.builder.position_at_end(continue_bb)

    def visit_BinOpNode(self, node: BinOpNode):
        left = node.left.accept(self)
        right = node.right.accept(self)

        # Logical / bitwise operators (parser tags these with Arabic words or symbols).
        if node.op in ('و', '&'):
            return self.builder.and_(left, right)
        if node.op in ('أو', '|'):
            return self.builder.or_(left, right)
        if node.op == '^':
            return self.builder.xor(left, right)
        if node.op == '<<':
            return self.builder.shl(left, right)
        if node.op == '>>':
            return self.builder.ashr(left, right)

        # Arithmetic / comparison: make operand types consistent first.
        left, right = self._unify_numeric(left, right)
        is_float = (left.type == self.f64 or right.type == self.f64)

        if node.op == '+':
            return self.builder.fadd(left, right) if is_float else self.builder.add(left, right)
        elif node.op == '-':
            return self.builder.fsub(left, right) if is_float else self.builder.sub(left, right)
        elif node.op == '*':
            return self.builder.fmul(left, right) if is_float else self.builder.mul(left, right)
        elif node.op == '/':
            if is_float:
                # Float division by zero yields ±inf/NaN, not a hardware fault,
                # so no trap is needed for floating-point division.
                return self.builder.fdiv(left, right)
            # Integer division: plant the divide-by-zero trap before sdiv.
            zero_val = ir.Constant(self.i32, 0)
            is_zero = self.builder.icmp_signed('==', right, zero_val, name="is_zero_trap")
            self.emit_runtime_trap(is_zero)
            # The cursor is now safely inside 'math_block'; divide is unreachable
            # unless the denominator was proven non-zero.
            return self.builder.sdiv(left, right, name="divtmp")
        elif node.op == '==':
            return self.builder.fcmp_ordered('==', left, right) if is_float else self.builder.icmp_signed('==', left, right)
        elif node.op == '!=':
            return self.builder.fcmp_ordered('!=', left, right) if is_float else self.builder.icmp_signed('!=', left, right)
        elif node.op == '<':
            return self.builder.fcmp_ordered('<', left, right) if is_float else self.builder.icmp_signed('<', left, right)
        elif node.op == '>':
            return self.builder.fcmp_ordered('>', left, right) if is_float else self.builder.icmp_signed('>', left, right)
        elif node.op == '<=':
            return self.builder.fcmp_ordered('<=', left, right) if is_float else self.builder.icmp_signed('<=', left, right)
        elif node.op == '>=':
            return self.builder.fcmp_ordered('>=', left, right) if is_float else self.builder.icmp_signed('>=', left, right)

        raise Exception(f"خطأ هندسي: عملية غير مدعومة '{node.op}'.")

    def visit_UnaryOpNode(self, node: UnaryOpNode):
        val = node.expr.accept(self)
        op = node.op

        if op == '+':
            return val
        if op == '-':
            if val.type == self.f64:
                return self.builder.fneg(val, name="neg")
            return self.builder.neg(val, name="neg")
        if op in ('!', 'ليس', 'لا'):
            # Logical NOT.
            if val.type == self.i1:
                return self.builder.not_(val, name="lnot")
            zero = ir.Constant(val.type, 0)
            return self.builder.icmp_signed('==', val, zero, name="lnot")
        if op == '~':
            return self.builder.not_(val, name="bnot")

        raise Exception(f"خطأ هندسي: عملية أحادية غير مدعومة '{op}'.")

    def visit_BoolNode(self, node: BoolNode):
        return ir.Constant(self.i1, 1 if node.value else 0)

    def visit_ContinueNode(self, node: ContinueNode):
        if not self.loop_stack:
            raise Exception("خطأ نحوي: تم استخدام أمر 'استمر' خارج حلقة تكرار")
        cond_bb, _ = self.loop_stack[-1]
        self.builder.branch(cond_bb)

    def visit_BreakNode(self, node: BreakNode):
        if not self.loop_stack:
            raise Exception("خطأ نحوي: تم استخدام أمر 'اقطع' خارج حلقة تكرار")
        _, end_bb = self.loop_stack[-1]
        self.builder.branch(end_bb)

    def visit_ReturnNode(self, node: ReturnNode):
        ret_type = self.builder.function.function_type.return_type
        if node.value is not None:
            val = node.value.accept(self)
            val = self._cast_value(val, ret_type)
            self.builder.ret(val)
        else:
            self.builder.ret_void()

    def visit_CharNode(self, node: CharNode):
        code = ord(node.value) if node.value else 0
        return ir.Constant(self.i8, code)

    def visit_IdNode(self, node: IdNode):
        # Arduino hardcoded constants.
        if node.name in ("عالي", "مخرج"):
            return ir.Constant(self.i32, 1)
        elif node.name in ("منخفض", "مدخل"):
            return ir.Constant(self.i32, 0)

        # Hardware register read (volatile 8-bit load, widened to i32).
        if node.name in self.registers:
            ld = self.builder.load(self.registers[node.name], name=node.name + "_val")
            ld.volatile = True
            return self.builder.zext(ld, self.i32, name=node.name + "_ext")

        ptr = self.llvm_env[node.name]
        return self.builder.load(ptr, name=node.name + "_val")

    def visit_NumberNode(self, node: NumberNode):
        if node.resolved_type == FLOAT_TYPE:
            return ir.Constant(self.f64, float(node.value))
        # Default to i32 (covers INT_TYPE and the un-resolved case).
        return ir.Constant(self.i32, int(node.value))

    def visit_StringNode(self, node: StringNode):
        return self._make_global_string(node.value)

    def visit_ImportNode(self, node: ImportNode):
        # Library symbols (e.g. سيريال) are pre-declared in _declare_builtins,
        # so import statements need no IR of their own.
        pass
