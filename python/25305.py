import sys

n, k = map(int, sys.stdin.readline().split())
grade = sys.stdin.readline().split()
for i in range(len(grade)):
    grade[i] = int(grade[i])

grade.sort(reverse=True)
print(grade[k-1])
