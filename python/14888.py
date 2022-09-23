from sys import stdin

input = stdin.readline
n = int(input().rstrip())
number = list(map(int, input().rstrip().split()))
operator = list(map(int, input().rstrip().split()))
maximum = -1e9
minimum = 1e9

def Calculation(a, result, plus, sub, multi, divide):
    global maximum, minimum
    if a == n:
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        return
    
    if plus:
        Calculation(a+1, result+number[a], plus-1, sub, multi, divide)
    if sub:
        Calculation(a+1, result-number[a], plus, sub-1, multi, divide)
    if multi:
        Calculation(a+1, result*number[a], plus, sub, multi-1, divide)
    if divide:
        Calculation(a+1, int(result/number[a]), plus, sub, multi, divide-1)
    
Calculation(1, number[0], operator[0], operator[1], operator[2], operator[3])
print(maximum)
print(minimum)