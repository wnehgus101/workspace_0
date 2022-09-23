def number_count(x,y):
    count = 0
    while x != 0:
        x = x//y
        count += x
    return count

m, n = map(int, input().split())

count_5 = number_count(m, 5) - number_count(n, 5) - number_count(m-n, 5)
count_2 = number_count(m, 2) - number_count(n, 2) - number_count(m-n, 2)

if count_5 > count_2:
    print(count_2)
else:
    print(count_5)