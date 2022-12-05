import socket
import time

maze_number = 1

def getXPosition(board, board_number_rows, board_number_colls):

    for i in range(board_number_rows):
        for j in range(board_number_colls):
            if(board[i][j] == 'X'):
                return (i,j)
    print("No X found")

def processNextMove(board, board_number_rows, board_number_colls, clientsocket, previous_move):
    x_position = getXPosition(board, board_number_rows, board_number_colls)

    i = x_position[0]
    j = x_position[1]
    if(board[i][j] == 'X'):
        while i < board_number_rows:
            while j < board_number_colls:
                if(previous_move <= j):
                    if(i+1 < board_number_rows and board[i+1][j] == 'O'):
                        clientsocket.send('V\n'.encode())
                        return j
                    elif(j+1 < board_number_colls and board[i][j+1] == 'O'):
                        clientsocket.send('>\n'.encode())
                        return j
                    elif(board[i][j-1] == 'O'):
                        clientsocket.send('<\n'.encode())
                        return j
                else:
                    if(i+1 < board_number_rows and board[i+1][j] == 'O'):
                        clientsocket.send('V\n'.encode())
                        return j
                    elif(j-1 >= 0 and board[i][j-1] == 'O'):
                        clientsocket.send('<\n'.encode())
                        return j
                    elif(board[i][j+1] == 'O'):
                        clientsocket.send('>\n'.encode())
                        return j

    else:
        print("Wrong X location")

def processBoard(board, clientsocket):
    previous_move = 0
    while True:
        board_number_rows = len(board)
        board_number_colls = len(board[0])
        previous_move = processNextMove(board, board_number_rows, board_number_colls, clientsocket, previous_move)
        board = proccessInput(clientsocket)
        if(board == True):
            return True


def proccessInput(clientsocket):
    data = b''
    while "Move:" not in data.decode():
        if("TUCTF" in data.decode()):
            print(data.decode())
            return
        data += clientsocket.recv(1024)

    decoded_data = data.decode()
    splited_data = decoded_data.split('\n')
    board = splited_data[1:len(splited_data)-1]
    if("Loading next level" in decoded_data):
        for i in range(len(splited_data)):
            if("Loading next level" in splited_data[i]):
                board = splited_data[i+2:len(splited_data)-1]
                global maze_number
                maze_number += 1
                print("New Maze:\n" + '\n'.join(board))
                return board
            elif("TUCTF" in decoded_data):
                print("FLAG FOUND!")
                print(decoded_data)
                return True
    print('\n'.join(board) + "\nMaze: " + str(maze_number))
    return board

def main():
    print("Challenge Shell Maze")
    start = time.time()
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('chals.tuctf.com', 30204))
    data = clientsocket.recv(1024)
    decoded_data = data.decode()
    splited_data = decoded_data.split('\n')
    board = splited_data[3:len(splited_data)-1]
    print("First board: " + "\n" + '\n'.join(board))
    processBoard(board, clientsocket)
    clientsocket.close()
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()
