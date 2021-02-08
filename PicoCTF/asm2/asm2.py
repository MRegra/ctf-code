'''
Stack:
[  local4 ]  <--- ebp-0x10
[  local3 ]  <--- ebp-0xc
[  local2 ]  <--- ebp-0x8
[  local1 ]  <--- ebp-0x4
[   ebp   ]
[   ret   ]  <--- ebp+0x4
[   arg1  ]  <--- ebp+0x8
[   arg2  ]  <--- ebp+0xc
'''
#We know that asm2 receives two arguments
def asm2(arg1, arg2):
#asm2:
	#<+0>:	push   ebp
	#<+1>:	mov    ebp,esp
	#<+3>:	sub    esp,0x10

	#<+6>:	mov    eax,DWORD PTR [ebp+0xc]
    eax = arg2

	#<+9>:	mov    DWORD PTR [ebp-0x4],eax
    local1 = eax

	#<+12>:	mov    eax,DWORD PTR [ebp+0x8]
    eax = arg1

	#<+15>:	mov    DWORD PTR [ebp-0x8],eax
    local2 = eax

	#<+18>:	jmp    0x509 <asm2+28>
	#<+20>:	add    DWORD PTR [ebp-0x4],0x1
	#<+24>:	sub    DWORD PTR [ebp-0x8],0xffffff80
    #<+28>:	cmp    DWORD PTR [ebp-0x8],0x63f3
	#<+35>:	jle    0x501 <asm2+20>
    while(local2 <= 0x63f3):
        local1 = (local1 + 1) & 0xffffffff              #This truncates the result to 32 bits.
        local2 = (local2 - 0xffffff80)  & 0xffffffff    #This truncates the result to 32 bits.           
    '''
    It is necessary to truncate the restuls because in python does not have
    buffer overflow but 0x86 can have so we have to truncate it.
    '''

	#<+37>:	mov    eax,DWORD PTR [ebp-0x4]
	#<+40>:	leave
	#<+41>:	ret
    return hex(local1)

print(asm2(0xb, 0x2e))