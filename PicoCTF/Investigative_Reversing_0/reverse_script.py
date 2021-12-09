"""
From the heddump we have:

70 69 63 6f 43 54 4b 80 6b 35 7a 73 69
p  i  c  o  C  T  K  .  k  5  z  s  i
64 36 71 5f 33 64 36 35 39 66 35 37 7d
d  6  q  _  3  d  6  5  9  f  5  7  }

"""

#This is the hexdump of the flag.
flag = "7069636f43544b806b357a73696436715f33643635396635377d"

length = len(flag)

lst = []

for i in range(0, length, 2):
    lst.append(flag[i:i+2])

for i in range(6):
    print(chr(int(lst[i], 16)), end='')

for i in range(6, 15):
     print(chr(int(lst[i], 16) - 5), end='')

print(chr(int(lst[15], 16) + 3), end='')

for i in range(16, 26):
    print(chr(int(lst[i], 16)), end='')

print()
