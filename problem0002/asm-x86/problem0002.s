# Problem: http://projecteuler.net/index.php?section=problems&id=2
# Author: Elie De Brauwer <elie @ de-brauwer.be>
# License: Simplified BSD
# Date: December 12, 2010


.section .data
.section .text
.globl _start
_start:
	movl $1, %eax         	# EAX = Fib_n-1
	movl $2, %ebx		# EBX = Fib_n
	movl $2, %ecx           # ECX = Result
start_loop:	
	cmpl $4000000, %ebx     # Only Fibonacci digits smaller than 4 million are allowed 
	jge out                 # Abort the loop when we reach the end
	xaddl %eax, %ebx        # Exchange and add instruction
	testl $1, %ebx          # Bitwise and between EBX and 1
	jnz start_loop          # When the AND is zero, then the last bit is not set, hence odd
add:	addl %ebx, %ecx         # Found an even Fiboannic number to add to the list
	jmp start_loop          # Next one please
out:	movl $1, %eax       	# 1 = exist system call
	movl $0, %ebx           # 0 = return code
	int $0x80
	