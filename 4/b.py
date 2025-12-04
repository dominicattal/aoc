with open("in2.txt", "r") as txt:
    G = []
    for line in txt.readlines():
        s = line.strip()
        G.append(s)
    m = len(G)
    n = len(G[0])
    C = [[-1] * n for _ in range(m)]
    D = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    Q = []
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
            C[i][j] = cnt
            if cnt < 4:
                Q.append((i,j))
    seen = set()
    res = 0
    while Q:
        i, j = Q.pop(0)
        if (i,j) in seen:
            continue
        seen.add((i,j))
        res += 1
        for di,dj in D:
            if not 0 <= i+di < m: continue
            if not 0 <= j+dj < n: continue
            if not G[i+di][j+dj] == '@': continue
            C[i+di][j+dj] -= 1
            if C[i+di][j+dj] < 4:
                Q.append((i+di,j+dj))
    print(res)
