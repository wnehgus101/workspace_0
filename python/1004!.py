import math

t = int(input())

for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for j in range(n):
        cx, cy, r = map(int, input().split())
        len_1 = math.sqrt((cx-x1)**2+(cy-y1)**2)
        len_2 = math.sqrt((cx-x2)**2+(cy-y2)**2)
        if (len_1 > r and len_2 < r) or (len_1 < r and len_2 > r):
            count += 1
    print(count)