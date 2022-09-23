dit1 = {}
def w (a, b ,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif (a,b,c) in dit1:
        return dit1[a,b,c]
    elif a < b and b < c:
        dit1[a,b,c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dit1[a,b,c]
    else:
        dit1[a,b,c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dit1[a,b,c]
    
a = 0
b = 0
c = 0
while True:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        break
    print(f"w({x}, {y}, {z}) = {w(x, y, z)}")
