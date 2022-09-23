from sys import stdin

input = stdin.readline
n = int(input().rstrip())
dp = [[0]*i for i in range(1, n+1)]
tri = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp[0] = tri[0]
if n > 1:
    dp[1][0] = tri[0][0] + tri[1][0]
    dp[1][1] = tri[0][0] + tri[1][1]
    for i in range(2, n):
        dp[i][0] = tri[i][0] + dp[i-1][0]
        dp[i][i] = tri[i][i] + dp[i-1][i-1]
        for j in range(1,i):
            dp[i][j] = tri[i][j] + max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[n-1]))