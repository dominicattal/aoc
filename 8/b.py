file = "in2.txt"
with open(file, "r") as txt:
    P = []
    for line in txt.readlines():
        s = line.strip()
        x,y,z = map(int, s.split(','))
        P.append((x,y,z))

    n = len(P)
    f = [i for i in range(n)]
    def find(x):
        if x == f[x]:
            return x
        f[x] = find(f[x])
        return f[x]
    def union(x,y):
        fx, fy = find(x), find(y)
        if fx != fy:
            f[fx] = fy

    conn = []
    for i in range(n):
        for j in range(i):
            dx = P[i][0]-P[j][0]
            dy = P[i][1]-P[j][1]
            dz = P[i][2]-P[j][2]
            d = dx*dx+dy*dy+dz*dz
            conn.append((d,i,j))
    conn.sort()
    
    def chk():
        for i in range(n-1):
            if find(i) != find(i+1):
                return False
        return True

    res = 0
    while not chk():
        d,i,j = conn.pop(0)
        union(i,j)
        res += 1
    print(P[i][0]*P[j][0])
    print(res)


# 0 7 19 14
# 13 2 18 17 8
# 12 9
# 16 11
