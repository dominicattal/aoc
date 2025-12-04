def toint(v):
    if v == '': return 0
    return int(v)
def DP(s):
    n = len(s)
    dp = [[""] * 13 for _ in range(n+1)]
    for i in range(1, n+1):
        for k in range(1,13):
            dp[i][k] = dp[i-1][k]
            for j in range(i):
                t = dp[j][k-1] + s[i-1]
                if toint(t) > toint(dp[i][k]):
                    dp[i][k] = t
    return toint(dp[n][12])

with open("in2.txt", "r") as txt:
    res = 0
    for line in txt.readlines():
        s = line.strip()
        res += DP(s)
    print(res)

