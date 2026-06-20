# codegen/llvm_generator.py
from llvmlite import ir
from ast_dir.visitor_interface import ASTVisitor
from ast_dir.nodes import *
from semantic.types_system import *

class LLVMIRGenerator(ASTVisitor):
    def __init__(self):
        # 1. Initialize the LLVM Module
        self.module = ir.Module(name="ar_arduino_module")
        self.module.triple = "avr-atmel-none"  # This is the target for Arduino Uno/Mega
        
        # 2. Setup the Builder (This is the tool that writes the instructions)
        self.builder = None 
        
        # 3. Environment for LLVM Pointers
        # We need to map Arabic variable names to their LLVM memory addresses (pointers)
        # Because LLVM IR is SSA (Static Single Assignment), variables are immutable. 
        # So we allocate memory, and save the pointer here to load/store later.
        self.llvm_env = {} 
        self.loop_stack = [] 
        
        # 4. Define LLVM Types (Mapping from our Semantic Types)
        self.i32 = ir.IntType(32)       # صحيح
        self.f64 = ir.DoubleType()      # عشري
        self.i1  = ir.IntType(1)        # منطقي (1 bit integer: 0 or 1)
        self.void = ir.VoidType()       # فارغ
        self.i8_ptr = ir.IntType(8).as_pointer() # مؤشر للنصوص (Strings)

        # 5. Pre-declare Arduino Built-in External Functions
        self._declare_builtins()


    
    def _get_llvm_type(self, semantic_type):
        """Helper function to map Arabic Types to LLVM Types"""
        if semantic_type == INT_TYPE: return self.i32
        if semantic_type == FLOAT_TYPE: return self.f64
        if semantic_type == BOOL_TYPE: return self.i1
        if semantic_type == STRING_TYPE: return self.i8_ptr
        return self.void

    def _declare_builtins(self):
        """Declare the C++ wrapper functions so LLVM knows they exist."""
        # c_digitalWrite(int pin, int val)
        func_type = ir.FunctionType(self.void, [self.i32, self.i32])
        self.c_digitalWrite = ir.Function(self.module, func_type, name="c_digitalWrite")

        # c_pinMode(int pin, int mode)
        func_type = ir.FunctionType(self.void, [self.i32, self.i32])
        self.c_pinMode = ir.Function(self.module, func_type, name="c_pinMode")

        # c_delay(int ms)
        func_type = ir.FunctionType(self.void, [self.i32])
        self.c_delay = ir.Function(self.module, func_type, name="c_delay")

    def get_ir(self):
        """Returns the final LLVM IR code as a string."""
        return str(self.module)

    def _get_llvm_type_from_string(self, type_str: str):
        """Helper to map Arabic string types from the AST to LLVM Types"""
        mapping = {
            'صحيح': self.i32,
            'رقم': self.i32,
            'عشري': self.f64,
            'كسري': self.f64,
            'نص': self.i8_ptr,
            'منطقي': self.i1,
            'فارغ': self.void
        }
        return mapping.get(type_str, self.void)
    
    
    def _cast_if_needed(self, val, target_llvm_type):
        """Helper to cast i32 to f64 if the target variable expects a float."""
        if val.type == self.i32 and target_llvm_type == self.f64:
            if self.builder is None:
                # We are in Global Scope, so we manually convert the constant
                return ir.Constant(self.f64, float(val.constant))
            else:
                # We are in a function, use the builder instruction
                return self.builder.sitofp(val, self.f64, name="cast_to_float")
        return val
    # ==========================================
    # Node Visiting Methods
    # ==========================================
    
    def visit_ProgramNode(self, node: ProgramNode):
        """Entry point for the AST."""
        for decl in node.declarations:
            decl.accept(self)
            
    def visit_VarDeclNode(self, node: VarDeclNode):
        # 1. Get the LLVM type (e.g., i32 for 'صحيح')
        llvm_type = self._get_llvm_type_from_string(node.var_type)
        
        # ==========================================
        # CASE 1: GLOBAL VARIABLE (Outside functions)
        # ==========================================
        if self.builder is None:
            # Create a global variable in the module
            ptr = ir.GlobalVariable(self.module, llvm_type, name=node.name)
            ptr.linkage = 'internal'  # Private to this module
            
            if node.value:
                # Evaluate the constant value (e.g., NumberNode returns ir.Constant)
                val = node.value.accept(self)
                val = self._cast_if_needed(val, llvm_type)
                ptr.initializer = val
            else:
                # If no value is given (e.g. متغير س : صحيح ؛), initialize with 0
                ptr.initializer = ir.Constant(llvm_type, None)
                
            # Save it to the environment
            self.llvm_env[node.name] = ptr

        # ==========================================
        # CASE 2: LOCAL VARIABLE (Inside a function)
        # ==========================================
        else:
            # Allocate memory on the stack
            ptr = self.builder.alloca(llvm_type, name=node.name)
            self.llvm_env[node.name] = ptr
            
            if node.value:
                # Evaluate the expression
                val = node.value.accept(self)
                val = self._cast_if_needed(val, llvm_type)
                # Store the value in the allocated pointer
                self.builder.store(val, ptr)

    def visit_AssignNode(self, node: AssignNode):
        # 1. Evaluate the right side of the equals sign
        val = node.value.accept(self)
        
        # 2. Find the variable's memory pointer in our environment
        ptr = self.llvm_env[node.name]
        target_llvm_type = self._get_llvm_type(node.resolved_type)
        val = self._cast_if_needed(val, target_llvm_type)
        # 3. Store the new value into the memory pointer
        self.builder.store(val, ptr)
        return val
    
    
    def visit_FuncDeclNode(self, node: FuncDeclNode):
        # 1. Translate Arduino-specific entry points
        llvm_func_name = node.name
        if node.name == 'اعداد':
            llvm_func_name = 'setup'
        elif node.name == 'تكرار':
            llvm_func_name = 'loop'

        # 2. Get Return Type and Parameter Types
        ret_type = self._get_llvm_type_from_string(node.return_type)
        param_types = [self._get_llvm_type_from_string(p[1]) for p in node.params]
    
        # 3. Create the Function Type and Function Instance
        func_type = ir.FunctionType(ret_type, param_types)
        func = ir.Function(self.module, func_type, name=llvm_func_name)

        # Name the parameters in LLVM for readability (e.g., %رقم)
        for i, arg in enumerate(func.args):
            arg.name = node.params[i][0]

        # 4. Create an 'entry' block and attach the Builder
        block = func.append_basic_block(name="entry")
        
        # Save previous builder and environment so we don't mess up global scoping
        previous_builder = self.builder
        previous_env = self.llvm_env.copy() 
        
        # Point our builder to write instructions inside this new block!
        self.builder = ir.IRBuilder(block)

        # 5. Allocate memory for function parameters
        for i, arg in enumerate(func.args):
            arg_name = node.params[i][0]
            # Allocate memory on the stack
            ptr = self.builder.alloca(arg.type, name=arg_name + "_ptr")
            # Store the passed argument value into this memory
            self.builder.store(arg, ptr)
            # Save the memory pointer in our environment so we can find it later!
            self.llvm_env[arg_name] = ptr

        # 6. Visit the Function Body (which is a BlockNode)
        if node.body:
            node.body.accept(self)

        # 7. LLVM CRITICAL SAFETY RULE: Every block MUST end with a return or branch!
        # If the user forgot to write "ارجع؛", we add it for them to prevent LLVM crashing.
        if not self.builder.block.is_terminated:
            if ret_type == self.void:
                self.builder.ret_void() 
            else:
                # If they forgot to return a number, return 0 as a default fallback
                self.builder.ret(ir.Constant(ret_type, 0))

        # 8. Restore the previous builder and environment
        self.builder = previous_builder
        self.llvm_env = previous_env
        
    
    def visit_BlockNode(self, node: BlockNode):
        """Visit all statements inside a {} block."""
        for stmt in node.statements:
            stmt.accept(self)

    def visit_FuncCallNode(self, node: FuncCallNode): pass
    
    def visit_IfNode(self, node: IfNode): 
        cond_val = node.condition.accept(self)
        current_function = self.builder.function
        then_bb = current_function.append_basic_block("then")
        merge_bb = current_function.append_basic_block("ifcont")
        if node.else_block:
            else_bb = current_function.append_basic_block("else")
            self.builder.cbranch(cond_val, then_bb, else_bb)
        else:
            self.builder.cbranch(cond_val,then_bb,merge_bb)
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

    # 1. Create the three blocks
        cond_bb = current_func.append_basic_block("while_cond")
        body_bb = current_func.append_basic_block("while_body")
        end_bb = current_func.append_basic_block("while_end")

    # 2. Jump to loop condition
        self.builder.branch(cond_bb)

    # 3. Generate condition block
        self.builder.position_at_end(cond_bb)

        cond_val = node.condition.accept(self)
        if cond_val is None:
            raise Exception("خطأ هندسي: تعذر تقييم شرط الحلقة.")

        # Conditional branch
        self.builder.cbranch(cond_val, body_bb, end_bb)

        # 4. Generate body block
        self.builder.position_at_end(body_bb)

    # Push current loop information
        self.loop_stack.append((cond_bb, end_bb))

    # Visit loop body
        node.body.accept(self)

    # Pop loop information
        self.loop_stack.pop()

    # 5. Back-edge to condition
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_bb)

    # 6. Continue after loop
        self.builder.position_at_end(end_bb)
        
    
    
    def visit_BinOpNode(self, node: BinOpNode):
        # 1. Get the LLVM values for the left and right sides
        left = node.left.accept(self)
        right = node.right.accept(self)
        
        # 2. USE OUR SEMANTIC AST TYPES! 
        # (Make sure FLOAT_TYPE is imported from semantic.types_system)
        is_float = (node.left.resolved_type == FLOAT_TYPE)
        
        # 3. Generate Math Instructions
        if node.op == '+':
            return self.builder.fadd(left, right) if is_float else self.builder.add(left, right)
        elif node.op == '-':
            return self.builder.fsub(left, right) if is_float else self.builder.sub(left, right)
        elif node.op == '*':
            return self.builder.fmul(left, right) if is_float else self.builder.mul(left, right)
        elif node.op == '/':
            return self.builder.fdiv(left, right) if is_float else self.builder.sdiv(left, right)
            
        # 4. Generate Comparison Instructions
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
        
        
    def visit_BoolNode(self, node: BoolNode): pass
    def visit_ContinueNode(self, node:ContinueNode):
        if not self.loop_stack:
            raise Exception("خطأ نحوي: تم استخدام أمر 'تجاوز' خارج حلقة تكرار")

    # Get condition block of current loop
        cond_bb, _ = self.loop_stack[-1]
        self.builder.branch(cond_bb)
        
    def visit_BreakNode(self, node:BreakNode):
        if not self.loop_stack:
            raise Exception("خطأ نحوي: تم استخدام أمر 'اكسر' خارج حلقة تكرار")
         # Get end block of current loop
        _, end_bb = self.loop_stack[-1]
        self.builder.branch(end_bb)
    def visit_ReturnNode(self, node: ReturnNode): pass
    def visit_CharNode(self, node: CharNode): pass
    def visit_IdNode(self, node: IdNode):
        # 1. Check if it's an Arduino hardcoded constant!
        if node.name in ["عالي", "مخرج"]:
            return ir.Constant(self.i32, 1)
        elif node.name in ["منخفض", "مدخل"]:
            return ir.Constant(self.i32, 0)
            
        # 2. If it's a normal variable, grab its pointer and LOAD the value
        ptr = self.llvm_env[node.name]
        return self.builder.load(ptr, name=node.name + "_val")

    def visit_NumberNode(self, node: NumberNode):
        # If it's a whole number, return i32. If it has decimals, return f64.
        if node.resolved_type == INT_TYPE:
            return ir.Constant(self.i32, int(node.value))
        elif node.resolved_type == FLOAT_TYPE:
            return ir.Constant(self.f64, float(node.value))
        
    def visit_ImportNode(self, node: ImportNode): pass
    def visit_StringNode(self, node: StringNode): pass
    def visit_UnaryOpNode(self, node: UnaryOpNode): pass
    
    
    