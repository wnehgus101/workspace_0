from sys import stdin

input = stdin.readline
standard = int(input().rstrip()) # 1m^2 당 참외의 개수
move = [list(map(int, input().split())) for _ in range(6)]
# 임의의 한 꼭지점에서 이동하는 것

width_max = 0; w_max_ind = 0
vertical_max =0; v_max_ind = 0

for i in range(6):
    if move[i][0] == 1 or move[i][0] == 2:
        if move[i][1] > width_max:
            width_max = move[i][1]
            w_max_ind = i
    else:
        if move[i][1] > vertical_max:
            vertical_max = move[i][1]
            v_max_ind = i

total = width_max * vertical_max
w_small_square = abs(move[(w_max_ind+1)%6][1] - move[(w_max_ind-1)%6][1] 
)
v_small_square = abs(move[(v_max_ind+1)%6][1] - move[(v_max_ind-1)%6][1] 
)
print((total-w_small_square*v_small_square)*standard)
