from collections import Counter
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
    
    for a in range(1000):
        d,i,j = conn[a]
        union(i,j)

    res = 1
    cnts = [0] * n
    for i in range(n):
        cnts[find(i)] += 1
    cnts.sort(reverse=True)
    print(cnts[0]*cnts[1]*cnts[2])


# 0 7 19 14
# 13 2 18 17 8
# 12 9
# 16 11
