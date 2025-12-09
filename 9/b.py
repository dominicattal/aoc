from math import inf 
file = "in2.txt"
with open(file, "r") as txt:
    S = []
    for line in txt.readlines():
        s = line.strip()
        x,y = map(int, s.split(','))
        S.append((x,y))
    minx = min([s[0] for s in S])
    miny = min([s[1] for s in S])
    maxx = max([s[0] for s in S])
    maxy = max([s[1] for s in S])
    rangesX = []
    rangesY = []
    for i in range(len(S)):
        x1,y1 = S[i]
        x2,y2 = S[(i+1)%len(S)]
        if x1 == x2:
            rangesY.append((x1,min(y1,y2),max(y1,y2)))
        else:
            rangesX.append((y1,min(x1,x2),max(x1,x2)))
    rangesX.sort()
    rangesY.sort()

    m,n = maxy, maxx
    minY = [inf] * (m+1)
    maxY = [-inf] * (m+1)
    minX = [inf] * (n+1)
    maxX = [-inf] * (n+1)
    for x,y1,y2 in rangesY:
        for j in range(y1,y2+1):
            minY[j] = min(minY[j], x)
            maxY[j] = max(maxY[j], x)
    for y,x1,x2 in rangesX:
        for j in range(x1,x2+1):
            minX[j] = min(minX[j], y)
            maxX[j] = max(maxX[j], y)
    res = 0
    def valid(x1,x2,y1,y2):
        for y in range(y1,y2+1):
            if not minY[y] <= x1 <= x2 <= maxY[y]:
                return False
        for x in range(x1,x2+1):
            if not minX[x] <= y1 <= y2 <= maxX[x]:
                return False
        return True
    for i in range(len(S)):
        print(i)
        x1,y1 = S[i]
        for j in range(i):
            x2,y2 = S[j]
            xx1, xx2 = min(x1,x2), max(x1,x2)
            yy1, yy2 = min(y1,y2), max(y1,y2)
            # (xx1,yy1) (xx1,yy2) (xx2,yy1) (xx2,yy2)
            if not valid(xx1,xx2,yy1,yy2):
                continue
            dx = abs(S[i][0] - S[j][0])
            dy = abs(S[i][1] - S[j][1])
            res = max(res, abs((dx+1)*(dy+1)))
    print(res)


