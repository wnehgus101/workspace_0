import sys
from collections import defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())
dic = defaultdict(lambda:0)
array_n = []
array_m = []
array_answer = []

for i in range(n):
    array_n.append(input())

for i in range(m):
    array_m.append(input())

for i in range(len(array_n)):
    dic[array_n[i]] = 1
    
for i in array_m:
    array_answer.append(dic[i])

print(array_answer.count(1))
