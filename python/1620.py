import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
    a = input().rstrip()
    dic[i] = a
    dic[a] = i

for i in range(m):
    b = input().rstrip()
    if b.isdigit():
        b = int(b)
        print(dic[b])
    else:
        print(dic[b])
