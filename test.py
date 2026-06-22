import llvmlite.binding as llvm 
llvm.initialize_all_targets()
print(llvm.Target.from_triple("avr-atmel-none"))   # RuntimeError if AVR is absent