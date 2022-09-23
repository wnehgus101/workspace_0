from itertools import permutations

n ,m = map(int, input().split())
n_arr = [i for i in range(1,n+1)]

for i in permutations(n_arr, m):
    print(*list(i))
