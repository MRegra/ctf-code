# This program is intended to convert a list of Numbers to the associated letter values. 

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

length = len(letters)

list_To_convert = [16, 9, 3, 15, 3, 20, 6, "{", 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, "}"]

for i in list_To_convert:
    if(not isinstance(i, int)):
        print(i, end = '')
    else:
        print(letters[i-1], end = '')
print()    



