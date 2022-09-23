import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input().rstrip())
dic = defaultdict(lambda:0)
array_n = list(map(int, input().split()))
m = int(input().rstrip())
array_m = list(map(int, input().split()))

for i in array_n:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in array_m:
    print(dic[i], end=' ')
