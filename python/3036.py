import math

n = int(input())
ring_arr = list(map(int, input().split()))
a = ring_arr[0]

for i in range(1,len(ring_arr)):
    b = a // math.gcd(a, ring_arr[i])
    c = ring_arr[i] // math.gcd(a, ring_arr[i])
    print(f"{b}/{c}")