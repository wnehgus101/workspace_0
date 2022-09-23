from sys import stdin

input = stdin.readline
string = input().rstrip()
a = set()

for i in range(len(string)):
    for j in range(i, len(string)):
        a.add(string[i:j+1])

print(len(a))
