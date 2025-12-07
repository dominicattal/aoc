file = "in2.txt"
with open(file, "r") as txt:
    G = []
    for line in txt.readlines():
        s = line.strip()
        G.append(s)
    for i in range(len(G)):
        if G[0][i] == 'S':
            break
    Q = [(0,i)] 
    res = 0
    seen = set()
    while Q:
        i,j = Q.pop(0)
        if i >= len(G) or j >= len(G[0]):
            continue
        if (i,j) in seen:
            continue
        seen.add((i,j))
        if G[i][j] == '^':
            res += 1
            Q.append((i+1,j-1))
            Q.append((i+1,j+1))
        else:
            Q.append((i+1,j))
    print(res)
