n = list(input())
a = []

for i in range(len(n)):
    a.append(int(n[i]))

a = sorted(a, reverse = True)
b = []
for i in range(len(a)):
    b.append(str(a[i]))
    
print(''.join(b))
