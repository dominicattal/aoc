from heapq import heappush, heappop
file = "in2.txt"
with open(file, "r") as txt:
    G = []
    for line in txt.readlines():
        G.append(line.strip())
    m,n = len(G), len(G[0])
    portals_rowwise = [[] for _ in range(m)]
    portals_colwise = [[] for _ in range(n)]
    for row in range(m):
        for col in range(n):
            if G[row][col] == 'O':
                portals_rowwise[row].append(col)
    for col in range(n):
        for row in range(m):
            if G[row][col] == 'O':
                portals_colwise[col].append(row)
    target = (n-2,m-2)
    pq = []
    D = [(0,1),(0,-1),(1,0),(-1,0)]
    S = ["S","N","E","W"]
    heappush(pq, (0,1,1,"",""))
    seen = set()
    while pq:
        cnt,x,y,path,code = heappop(pq)
        if (x,y) == target:
            print(cnt)
            print(code)
            print(path)
            break
        if (x,y) in seen:
            continue
        seen.add((x,y))
        for i,(dx,dy) in enumerate(D):
            nx, ny = x+dx, y+dy
            if not 0 <= nx < n:
                continue
            if not 0 <= ny < m:
                continue
            if G[ny][nx] == '#':
                continue
            if G[ny][nx] == 'X':
                heappush(pq, (cnt+5,nx,ny,path+S[i],code))
            elif G[ny][nx] == 'O':
                for px in portals_rowwise[ny]:
                    heappush(pq, (cnt+1,px,ny,path+S[i],code))
                for py in portals_colwise[nx]:
                    heappush(pq, (cnt+1,nx,py,path+S[i],code))
            else:
                new_code = code if G[ny][nx] == ' ' else code+G[ny][nx]
                heappush(pq, (cnt+1,nx,ny,path+S[i],new_code))



