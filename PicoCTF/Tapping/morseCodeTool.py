
morse_code_alphabet = {".-" : 'A',
                      "-..." : 'B',
                      "-.-." : 'C',
                      "-.." : 'D',
                      "." : 'E',
                      "..-." : 'F',
                      "--." : 'G',
                      "...." : 'H',
                      ".." : 'I',
                      ".---" : 'J',
                      "-.-" : 'K',
                      ".-.." : 'L',
                      "--" : 'M',
                      "-." : 'N',
                      "---" : 'O',
                      ".--." : 'P',
                      "--.-" : 'Q',
                      ".-." : 'R',
                      "..." : 'S',
                      "-" : 'T',
                      "..-" : 'U',
                      "...-" : 'V',
                      ".--" : 'W',
                      "-..-" : 'X',
                      "-.--" : 'Y',
                      "--.." : 'Z',
                      ".----" : '1',
                      "..---" : '2',
                      "...--" : '3',
                      "....-" : '4',
                      "....." : '5',
                      "-...." : '6',
                      "--..." : '7',
                      "---.." : '8',
                      "----." : '9',
                      "-----" : '0',}

def encode():
    morse_code_message = input("Message to encode: ")
    for key,value in morse_code_alphabet.items():
        for i in morse_code_message:
            if(value == i):
                print(key + " ", end='')
    print()


def decode():
    morse_code_message = input("Message to decode: ")
    message_chars_list = morse_code_message.split( )
    for i in message_chars_list:
        if(i == "{" or i == "}"):
            print(i, end='')
        else:    
            for key in morse_code_alphabet:
                if(i == key):
                    print(morse_code_alphabet[key], end='')
    print()




def main():
    print("Welcome to the morse code tool")
    print("Menu:")
    print("1 - Encode")
    print("2 - Decode")
    option = input("Choose one option: ")
    if(option == str(1)):
        encode()
    elif(option == str(2)):
        decode()
    else:
        print("Wrong option, try again.")
        main()

if __name__ == "__main__":
    main()