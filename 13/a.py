file = "in1.txt"
with open(file, "r") as txt:
    G = []
    for line in txt.readlines():
        G.append(line.strip())
    m,n = len(G), len(G[0])
    target = (n-2,m-2)
    q = [(0,1,1)]
    D = [(0,1),(0,-1),(1,0),(-1,0)]
    seen = set()
    while q:
        cnt,x,y = q.pop(0)
        if (x,y) == target:
            print(cnt)
            break
        if (x,y) in seen:
            continue
        seen.add((x,y))
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if not 0 <= nx < n:
                continue
            if not 0 <= ny < m:
                continue
            if G[ny][nx] in '#XO':
                continue
            q.append((cnt+1,nx,ny))


