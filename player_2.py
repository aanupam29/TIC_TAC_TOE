import socket

print("Player - 2")

while True:
    c2 = socket.socket()
    c2.connect(('localhost', 9997))
    s = c2.recv(1024).decode()
    print(s)
    str = list(s)

    while True:
        print("Which row and column do you want to add X? ")
        row, col = map(int, input().split())
        row = row-1
        col = col-1
        index = 4*row + col
        if row < 0 or row > 2 or col < 0 or col > 2:
            continue
        if str[index] != '.':
            continue
        str[index] = 'X'
        break

    s = ''.join(str)
    print(s)
    c2.send(bytes(s, 'utf-8'))
