n = int(input())
array = []

for i in range(1, n*1000):
    if str(i).count('666') == 1:
        array.append(i)

print(array[n-1])