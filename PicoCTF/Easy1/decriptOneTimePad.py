alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = "SOLVECRYPTO"

encrypted_flag = "UFJKXQZQUNB"

length_text = len(encrypted_flag)

for i in range(length_text):
	if((ord(encrypted_flag[i])-ord(key[i]))>=0):
		print(chr(ord(encrypted_flag[i])-ord(key[i])+65), end='')
	elif((ord(encrypted_flag[i])-ord(key[i])) < 0):
		print(chr(ord(encrypted_flag[i])-ord(key[i])+91), end='')	
print()