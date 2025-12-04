with open("in2.txt", "r") as txt:
    G = []
    for line in txt.readlines():
        s = line.strip()
        G.append(s)
    m = len(G)
    n = len(G[0])
    D = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    res = 0
    for i in range(m):
        for j in range(n):
            if not G[i][j] == '@':
                continue
            cnt = 0
            for di,dj in D:
                if not 0 <= i+di < m: continue
                if not 0 <= j+dj < n: continue
                if not G[i+di][j+dj] == '@': continue
                cnt += 1
            if cnt < 4:
                res += 1
    print(res)
