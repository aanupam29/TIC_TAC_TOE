import socket


def chk(str):
    if str[0] == str[1] and str[1] == str[2] and str[0] != '.':
        return 1
    if str[4] == str[5] and str[5] == str[6] and str[4] != '.':
        return 1
    if str[8] == str[9] and str[10] == str[9] and str[8] != '.':
        return 1
    if str[0] == str[4] and str[4] == str[8] and str[0] != '.':
        return 1
    if str[1] == str[5] and str[5] == str[9] and str[1] != '.':
        return 1
    if str[2] == str[6] and str[6] == str[10] and str[2] != '.':
        return 1
    if str[0] == str[5] and str[5] == str[10] and str[0] != '.':
        return 1
    if str[2] == str[5] and str[5] == str[8] and str[2] != '.':
        return 1
    return 0

def chk2(s):
    if s[0]=='.' or s[1]=='.' or s[2]=='.' or s[4]=='.' or s[5]=='.' or s[6]=='.' and s[8]=='.' or s[9]=='.' or s[10]=='.':
        return 0
    return 1


s = socket.socket()
s.bind(('localhost', 9997))
s.listen(1000)
print("Welcome...")

mat = "...\n...\n...\n"
while True:
    c1, addr1 = s.accept()
    c1.send(bytes(mat, 'utf-8'))
    mat = c1.recv(1024).decode()
    print(mat)
    val = chk(mat)
    if val == 1:
        print("Player-1 won")
        c1.close()
        s.close()
        break

    val2 = chk2(mat)
    if val2 == 1:
        print("TIE")
        break

    c2, addr2 = s.accept()
    c2.send(bytes(mat, 'utf-8'))
    mat = c2.recv(1024).decode()
    print(mat)
    val = chk(mat)
    if val == 1:
        print("Player-2 won")
        c2.close()
        s.close()
        break
