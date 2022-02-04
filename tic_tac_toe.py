s = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
n = 1
for i in range(3):
    for j in range(3):
        print(s[i][j], end=' ')
    print()

def draw():
    count = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != '-':
                count += 1
    return count == 9

while True:

    if n % 2 != 0:
        enter_x = list(map(int, input('Enter X').split()))
        for i in range(3):
            for j in range(3):
                if enter_x[0] == i and enter_x[1] == j:
                    if s[i][j] == '-':
                        s[i][j] = 'X'
                    else:
                        n -= 1

        for i in range(3):
            for j in range(3):
                print(s[i][j], end=' ')
            print()
        n += 1
        if s[1][1] == 'X' and s[0][0] == 'X' and s[2][2] == 'X':
            print('X win!')
            break
        elif s[0][0] == 'X' and s[0][1] == 'X' and s[0][2] == 'X':
            print('X win!')
            break
        elif s[1][0] == 'X' and s[1][1] == 'X' and s[1][2] == 'X':
            print('X win!')
            break
        elif s[2][0] == 'X' and s[2][1] == 'X' and s[2][2] == 'X':
            print('X win!')
            break
        elif s[0][0] == 'X' and s[1][0] == 'X' and s[2][0] == 'X':
            print('X win!')
            break
        elif s[0][1] == 'X' and s[1][1] == 'X' and s[2][1] == 'X':
            print('X win!')
            break
        elif s[0][2] == 'X' and s[1][2] == 'X' and s[2][2] == 'X':
            print('X win!')
            break
        elif s[2][0] == 'X' and s[1][1] == 'X' and s[0][2] == 'X':
            print('X win!')
            break
    else:
        enter_0 = list(map(int, input('Enter 0').split()))
        for i in range(3):
            for j in range(3):
                if enter_0[0] == i and enter_0[1] == j:
                    if s[i][j] == '-':
                        s[i][j] = '0'
                    else:
                        n -= 1

        for i in range(3):
            for j in range(3):
                print(s[i][j], end=' ')
            print()
        n += 1
        if s[1][1] == '0' and s[0][0] == '0' and s[2][2] == '0':
            print('0 win!')
            break
        elif s[0][0] == '0' and s[0][1] == '0' and s[0][2] == '0':
            print('0 win!')
            break
        elif s[1][0] == '0' and s[1][1] == '0' and s[1][2] == '0':
            print('0 win!')
            break
        elif s[2][0] == '0' and s[2][1] == '0' and s[2][2] == '0':
            print('0 win!')
            break
        elif s[0][0] == '0' and s[1][0] == '0' and s[2][0] == '0':
            print('0 win!')
            break
        elif s[0][1] == '0' and s[1][1] == '0' and s[2][1] == '0':
            print('0 win!')
            break
        elif s[0][2] == '0' and s[1][2] == '0' and s[2][2] == '0':
            print('0 win!')
            break
        elif s[2][0] == '0' and s[1][1] == '0' and s[0][2] == '0':
            print('0 win!')
            break
    if draw() == True:
        print('Draw')
        break


