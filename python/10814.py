n = int(input())
array = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    array.append([age, name])

array.sort(key=lambda x:x[0])

for i in array:
    print(*i)