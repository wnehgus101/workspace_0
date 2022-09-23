all = [list(map(int, input().split())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if all[i][j] == 0:
            zero.append((i, j))

def main(x):
    if x == len(zero):
        for i in range(9):
            print(*all[i])
        exit(0)
    
    for i in range(1, 10):
        a = zero[x][0]
        b = zero[x][1]
        if LineCheck(i,a) and RowCheck(i,b) and SquareCheck(a,b,i):
            all[a][b] = i
            main(x+1)
            all[a][b] = 0

def LineCheck(x,y):
    for i in range(9):
        if x == all[y][i]:
            return False
    return True

def RowCheck(x,y):
    for j in range(9):
        if x == all[j][y]:
            return False
    return True

def SquareCheck(x,y,f):
    nx = x//3*3
    ny = y//3*3
    for i in range(3):
        for j in range(3):
            if f == all[nx+i][ny+j]:
                return False
    return True

main(0)
