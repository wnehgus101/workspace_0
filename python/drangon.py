from sys import stdin

input = stdin.readline

letter_grade = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
break_point = [93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60, 0]
numeric_grades = list(map(int, input().rstrip().split()))

for i in numeric_grades:
    for j in range(12):
        if i >= break_point[j]:
            print(letter_grade[j])
            break
