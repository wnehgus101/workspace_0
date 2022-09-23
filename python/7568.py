n = int(input()) #n명의 집단
array_1 = []
array_3 = []

for i in range(n): #행렬 만들기
    x, y = map(int, input().split())
    array_2 = [x,y]
    array_1.append(array_2)

for i in range(n):
    a = 1
    for j in range(n):
        if array_1[i][0] < array_1[j][0] and array_1[i][1] < array_1[j][1]:
            a += 1
    array_3.append(a)
    
print(*array_3)