#This function reverse engineers the code.
def crackPassowrd():
    myBytes = [106, 85, 53, 116, 95, 52, 95, 98,
               0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
               0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o146, 0o64 ,
               'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ,]
    newMyBytes = []
    for val in myBytes:
        if(isinstance(val, int)):
            newMyBytes.append(chr(val))
        elif(str(val).startswith('0x')):
            newMyBytes.append(bytes.fromhex(val).decode('utf-8'))
        elif(str(val).startswith('0o')):
            newMyBytes.append(val)    
        elif(isinstance(val, str)):
            newMyBytes.append(val)
    return newMyBytes

#This function constructs the flag based on the crackPassword function
def getFlag(newMyBytes):
    res = "picoCTF{"
    for i in newMyBytes:
        res += i
    return res + "}"

print(getFlag(crackPassowrd()))
