# Problem: http://projecteuler.net/index.php?section=problems&id=1
# Author: Elie De Brauwer <elie @ de-brauwer.be>
# License: Simplified BSD
# Date: December 11, 2010


.section .data
.section .text
.globl _start
_start:
	movl $1, %ecx         	# Counter goes in ECX
	movl $0, %ebx		# Result goes in EBX
	movl $3, %esi           # Put 3 in esi
	movl $5, %edi           # Put 5 in edi
start_loop:	
	cmpl $1000, %ecx        # Try this amount of times
	je out                  # Abort the loop when we reach the end
	xor %edx, %edx          # Clear EDX
	movl %ecx, %eax         # Copy counter to EAX
# div divides %edx:%eax by %esi, the quotient goes in %eax and the remainder in %edx
	divl %esi               # Divide by ESI (3) 
	cmpl $0, %edx           # Check remainder
	je valid                # When zero this is valid.
	xor %edx, %edx          # Clear EDX
	movl %ecx, %eax         # Copy counter to EAX
	divl %edi               # Devide by EBI (5)
	cmpl $0, %edx           # Check remaind
	jne not_valid           # When zero goto valid, else goto not valid
valid:
	addl %ecx, %ebx         # Sum += i
not_valid:	
	inc %ecx		# Increment counter
	jmp start_loop          # Retry
out:
	movl $1, %eax       	# 1 = exist system call
	movl $0, %ebx           # 0 = return code
	int $0x80
	