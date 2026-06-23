; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-P1-p:16:8-i8:8-i16:8-i32:8-i64:8-f32:8-f64:8-n8-a:8"
target triple = "avr-atmel-none"

@"\D8\A7\D9\84\D8\B3\D8\B7\D9\88\D8\B9" = internal unnamed_addr global i32 0
@"\D9\85\D9\82\D8\AF\D8\A7\D8\B1_\D8\A7\D9\84\D8\AA\D9\84\D8\A7\D8\B4\D9\8A" = internal unnamed_addr global i32 5

declare void @c_pinMode(i32, i32) local_unnamed_addr addrspace(0)

declare void @c_analogWrite(i32, i32) local_unnamed_addr addrspace(0)

declare void @c_delay(i32) local_unnamed_addr addrspace(0)

define void @setup() local_unnamed_addr addrspace(0) {
entry:
  tail call addrspace(0) void @c_pinMode(i32 9, i32 1)
  ret void
}

define void @loop() local_unnamed_addr addrspace(0) {
entry:
  %"\D8\A7\D9\84\D8\B3\D8\B7\D9\88\D8\B9_val" = load i32, ptr @"\D8\A7\D9\84\D8\B3\D8\B7\D9\88\D8\B9", align 4
  tail call addrspace(0) void @c_analogWrite(i32 9, i32 %"\D8\A7\D9\84\D8\B3\D8\B7\D9\88\D8\B9_val")
  %"\D8\A7\D9\84\D8\B3\D8\B7\D9\88\D8\B9_val.1" = load i32, ptr @"\D8\A7\D9\84\D8\B3\D8\B7\D9\88\D8\B9", align 4
  %"\D9\85\D9\82\D8\AF\D8\A7\D8\B1_\D8\A7\D9\84\D8\AA\D9\84\D8\A7\D8\B4\D9\8A_val" = load i32, ptr @"\D9\85\D9\82\D8\AF\D8\A7\D8\B1_\D8\A7\D9\84\D8\AA\D9\84\D8\A7\D8\B4\D9\8A", align 4
  %.3 = add i32 %"\D9\85\D9\82\D8\AF\D8\A7\D8\B1_\D8\A7\D9\84\D8\AA\D9\84\D8\A7\D8\B4\D9\8A_val", %"\D8\A7\D9\84\D8\B3\D8\B7\D9\88\D8\B9_val.1"
  store i32 %.3, ptr @"\D8\A7\D9\84\D8\B3\D8\B7\D9\88\D8\B9", align 4
  %0 = add i32 %.3, -255
  %.7.avrbias = xor i32 %0, -2147483648
  %.7 = icmp slt i32 %.7.avrbias, 2147483394
  br i1 %.7, label %then, label %ifcont

then:                                             ; preds = %entry
  %neg = sub nsw i32 0, %"\D9\85\D9\82\D8\AF\D8\A7\D8\B1_\D8\A7\D9\84\D8\AA\D9\84\D8\A7\D8\B4\D9\8A_val"
  store i32 %neg, ptr @"\D9\85\D9\82\D8\AF\D8\A7\D8\B1_\D8\A7\D9\84\D8\AA\D9\84\D8\A7\D8\B4\D9\8A", align 4
  br label %ifcont

ifcont:                                           ; preds = %then, %entry
  tail call addrspace(0) void @c_delay(i32 30)
  tail call addrspace(0) void @c_delay(i32 20)
  ret void
}
