import math
n = int(input())
array = [int(input()) for _ in range(n)]
array.sort()
arr_sub = []
arr_m = []

for i in range(1,len(array)):
    arr_sub.append(array[i]-array[i-1])

agcd = arr_sub[0]

for i in range(1,len(arr_sub)):
    agcd = math.gcd(agcd, arr_sub[i])

for i in range(2,int(agcd**0.5)+1):
    if agcd % i == 0:
        arr_m.append(i)
        arr_m.append(agcd//i)
arr_m.append(agcd)
print(*sorted(list(set(arr_m))))
