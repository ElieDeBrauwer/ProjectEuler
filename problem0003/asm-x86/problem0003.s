# Problem: http://projecteuler.net/index.php?section=problems&id=3
# Author: Elie De Brauwer <elie @ de-brauwer.be>
# License: Simplified BSD
# Date: December 12, 2010


.section .data
.section .text
.globl _start
_start:
#>>> print "%x" % 600851475143
#8be589eac7
	movl $1000, %ecx        # ECX contains a counter, start by a large number to avoid overflow.
start:	movl $0x0000008b, %edx  # Initial value, MSB in EDX
        movl $0xe589eac7, %eax  # Initial value, LSB in EDX
	cmpl $0xffffffff, %ecx  # Abort when counter is getting too high
	je out                  
	divl %ecx               # Divide by counter
	test %edx, %edx         # Check if the modulo is 0
	jnz next                # If not 0, try the next one
	movl %ecx, %ebx         # This was a valid divisor, set it in EBX
next:	
	inc %ecx                # Increment counter
	jmp start               # Retry
out:	# Result in EBX
	movl $1, %eax       	# 1 = exist system call
	movl $0, %ebx           # 0 = return code
	int $0x80
	