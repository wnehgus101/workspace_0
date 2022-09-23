import math
w, h, x, y, p = map(int, input().split())
count = 0

for _ in range(p):
    x2, y2 = map(int, input().split())
    if math.sqrt((x-x2)**2+(y+h/2-y2)**2) <= h/2:
        count += 1
    elif math.sqrt((x+w-x2)**2+(y+h/2-y2)**2) <= h/2:
        count += 1
    elif abs(y+h/2-y2) <= h/2 and abs(x+w/2-x2) <= w/2:
        count += 1

print(count)
    