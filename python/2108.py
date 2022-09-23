import sys
from collections import Counter

n = int(sys.stdin.readline())
array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

cnt = Counter(array).most_common()
mode = []
for i in cnt:
    if i[1] == cnt[0][1]:
        mode.append(i)
    else:
        break

print(round(sum(array)/n))
print(array[n//2])
if len(mode) == 1:
    print(mode[0][0])
else:
    mode.sort()
    print(mode[1][0])
print(max(array)-min(array))
