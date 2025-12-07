file = "in2.txt"
with open(file, "r") as txt:
    G = []
    for line in txt.readlines():
        s = line.strip()
        G.append(s)
    for i in range(len(G)):
        if G[0][i] == 'S':
            break
    m, n = len(G), len(G[0])
    dp = [[0] * n for _ in range(m+1)]
    dp[0][i] = 1
    for i in range(1, m):
        for j in range(n):
            if G[i][j] == '^':
                if 0 <= j-1 < n:
                    dp[i][j-1] += dp[i-1][j]
                if 0 <= j+1 < n:
                    dp[i][j+1] += dp[i-1][j]
            else:
                dp[i][j] += dp[i-1][j]
    print(sum(dp[m-1]))
