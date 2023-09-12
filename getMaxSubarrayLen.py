def getMaxSubarrayLen(n, team_a, team_b):
    dp = [[1] * 2 for _ in range(n)]
    ans = 1
    for i in range(1, n):
        if team_a[i] >= team_a[i-1]:
            dp[i][0] = max(dp[i-1][0] + 1, dp[i][0])
            ans = max(ans, dp[i][0])
        elif team_a[i] >= team_b[i-1]:
            dp[i][0] = max(dp[i-1][1] + 1, dp[i][0])
            ans = max(ans, dp[i][0])
        if team_b[i] >= team_a[i-1]:
            dp[i][1] = max(dp[i-1][0] + 1, dp[i][1])
            ans = max(ans, dp[i][1])
        elif team_b[i] >= team_b[i-1]:
            dp[i][1] = max(dp[i-1][1] + 1, dp[i][1])
            ans = max(ans, dp[i][1])
    return ans


    

        