alphabet="abcdefghijklmnopqrstuvwxyz"

encrypted_flag = "gvswwmrkxlivyfmgsrhnrisegl"

length_text = len(encrypted_flag)

for j in range(26):
	for i in range(length_text):
		print(chr(((ord(encrypted_flag[i])-j)-97)%26+97), end='')
	print()	
print()
