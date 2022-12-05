import socket

def proccessMultiplications(data, total_multiplications):
    final_list = []
    tmp_list = data
    if(total_multiplications == 0):
        return data
    else:
        for i in range(0, len(data), 2):
            if(i+1 >= len(data)):
                if(tmp_list[i-1] == '+' or tmp_list[i-1] == '-'):
                    final_list.append(data[i])
                    break
                break
            if(tmp_list[i+1] == '+'):
                if(data[i] == None):
                    final_list.append(data[i+1])
                else:
                    final_list.append(data[i])
                    final_list.append(data[i+1])
            elif(tmp_list[i+1] == '-'):
                if(data[i] == None):
                    final_list.append(data[i+1])
                else:
                    final_list.append(data[i])
                    final_list.append(data[i+1])
            elif(tmp_list[i+1] == '*'):
                if(tmp_list[i] != None):
                    final_list.append(int(data[i]) * int(data[i+2]))
                    tmp_list[i] = None
                    tmp_list[i+2] = None
                elif(tmp_list[i-1] == '*'):
                    final_list.append(tmp_list[i+1])
                    final_list.append(tmp_list[i+2])
                    tmp_list[i+2] = None
                elif(tmp_list[i] == None):
                    continue

        new_total_multiplications = 0
        for i in final_list:
            if(i == '*'):
                new_total_multiplications += 1
        return proccessMultiplications(final_list, new_total_multiplications)

def processData(clientsocket, data):

    updated_list = proccessMultiplications(data, 1)
    length = len(updated_list)
    res = int(updated_list[0])
    for i in range(2, length, 2):
        temp = updated_list[i-1]
        if(temp == "+"):
            res += int(updated_list[i])
        elif(temp == "-"):
            res -= int(updated_list[i])

    output = str(res) + '\n'

    clientsocket.send(output.encode())

def main():
    print("Challenge Leisurely Math")
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('chals.tuctf.com', 30202))
    for i in range(2000):
        data = clientsocket.recv(1024)
        decoded_data = data.decode()
        print("Iteration: " + str(i) + " - " + decoded_data)
        test_cenas = decoded_data.split('\n')
        if("Incorrect!" in decoded_data):
            break
        elif(len(test_cenas) > 3):
            decoded_data = test_cenas[2].split( )
            processData(clientsocket, decoded_data)
        elif("TUCTF{" in decoded_data):
            print("THE FLAG FOUND: " + decoded_data)
            break
        elif("Correct!" in decoded_data):
            decoded_data = decoded_data.split( )
            processData(clientsocket, decoded_data[1:len(decoded_data)-1])
        else:
            decoded_data = decoded_data.split( )
            processData(clientsocket, decoded_data[0:len(decoded_data)-1])

    clientsocket.close()

if __name__ == "__main__":
    main()
