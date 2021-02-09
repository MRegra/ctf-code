
def convertSpacesToBinary():
    with open('whitepages.txt', 'rb') as f:
        result = f.read()
        result = result.replace(b'\xe2\x80\x83', b'0')
        result = result.replace(b'\x20', b'1')
        result = result.decode()
    return result    

def convertFromBinaryToASCII(binaryValues):

    binary_int = int(binaryValues, 2)
    byte_number = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode('ascii')

    print(ascii_text)

convertFromBinaryToASCII(convertSpacesToBinary())