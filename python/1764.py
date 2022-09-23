from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
dic_n = {}
dic_m = {}
answer = []

for i in range(n):
    dic_n[input().rstrip()] = i
    
for i in range(m):
    dic_m[input().rstrip()] = i
    
for i in dic_n:
    if i in dic_m:
        answer.append(i)

print(len(answer))
answer.sort()
for i in answer:
    print(i)
