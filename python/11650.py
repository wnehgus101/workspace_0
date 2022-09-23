n = int(input())
array = []

for i in range(n):
    xi, yi = map(int, input().split())
    array.append([xi, yi])

array.sort(key=lambda x: x[0])
for i in array:
    print(*i)