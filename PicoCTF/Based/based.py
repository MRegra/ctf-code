import binascii

def binaryToASCII():
    binary_input = input("What is the binary input to convert: ")
    splittedInputToIgnoreSpaces = ''.join(binary_input.split(' '))
    n = int(splittedInputToIgnoreSpaces, 2)
    print(binascii.unhexlify('%x' % n))

def eightBaseToASCII():
    octal_input = input("What is the octal input to convert: ")
    splittedInputToIgnoreSpaces = octal_input.split(' ')
    str_converted = ""
    for octal_char in splittedInputToIgnoreSpaces:
        str_converted += chr(int(octal_char, 8))
    print(str_converted)

def hexToASCII():
    hex_input = input("What is the decimal input to convert: ")
    print(bytes.fromhex(hex_input).decode('utf-8'))

def mainMenuDisplay():
    print("Welcome to the Based challenge script")
    print("Menu: ")
    print("1 - From binary to ASCII")
    print("2 - From octal to ASCII")
    print("3 - From hexadecimal to ASCII")
    print("0 - Exit")

def main():
    mainMenuDisplay()
    option = input("Choose one option: ")
    while(option != "0"):
        if(option == "1"):
            binaryToASCII()
        elif(option == "2"):
            eightBaseToASCII()
        elif(option == "3"):
            hexToASCII()    
        elif(option == "0"):
            print("Bye bye")
            break
        else:
            print("Something went wrong, bye")
            break
        mainMenuDisplay()
        option = input("Choose one option: ")

if __name__ == "__main__":
    main()