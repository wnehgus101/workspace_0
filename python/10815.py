import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
have = list(map(int, input().split()))
m = int(input())
compare = list(map(int, input().split()))
dic = defaultdict(lambda:0)

for i in range(len(have)):
    dic[have[i]] = 1

for j in compare:
    print(dic[j], end=' ')
