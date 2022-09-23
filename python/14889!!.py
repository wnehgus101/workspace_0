from sys import stdin
from itertools import combinations

n = int(input())
n_1 = [i for i in range(1,n+1)]
team = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
combi_0 = list(combinations(n_1, n//2))
combi_1 = list(combinations(n_1, n//2))[:len(combi_0)//2]
combi_2 = list(combinations(n_1, n//2))[len(combi_0)//2:]
combi_2.sort(reverse=True)
main = []
for i in range(len(combi_1)):
    a=0
    b=0
    for j in range(len(combi_1[i])):
        for k in range(len(combi_1[i])):
            a += team[combi_1[i][j]-1][combi_1[i][k]-1]
            b += team[combi_2[i][j]-1][combi_2[i][k]-1]
    main.append(abs(a-b))

print(min(main))