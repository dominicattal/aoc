file = "in2.txt"
with open(file, "r") as txt:
    S = []
    for line in txt.readlines():
        s = line.strip()
        x,y = map(int, s.split(','))
        S.append((x,y))
    res = 0
    for i in range(len(S)):
        for j in range(i):
            dx = abs(S[i][0] - S[j][0])
            dy = abs(S[i][1] - S[j][1])
            res = max(res, abs((dx+1)*(dy+1)))
    print(res)

