n, m = map(int, input().split())
square = []
change = []

for i in range(n):
    a = list(map(str, input()))
    square.append(a)

for i in range(n-7):
    for j in range(m-7):
        count_1 = 0
        count_2 = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2 == 0:
                    if square[k][l] != 'W':
                        count_1 += 1
                    elif square[k][l] != 'B':
                        count_2 += 1
                else:
                    if square[k][l] != 'B':
                        count_1 += 1
                    elif square[k][l] != 'W':
                        count_2 += 1
        change.append(min(count_1, count_2))

print(min(change))