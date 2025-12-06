file = "in2.txt"
with open(file, "r") as txt:
    R = []
    ops = None
    lens = []
    for line in txt.readlines():
        s = line[:-1]
        if line[0] not in '*+':
            R.append(s)
        else:
            ops = s
    pfx = [-1]
    res = 0
    m = max([len(a) for a in R])
    m = max(m, len(ops))
    while True:
        col = pfx[-1]+1
        if col >= m: break
        i = 0
        while i < len(R):
            if col >= len(R[i]):
                i += 1
            elif R[i][col] != ' ':
                col += 1
                i = 0
            else:
                i += 1
        l = col - pfx[-1] - 1
        b = ops[pfx[-1]+1] == '*'
        a = 0
        if b:
            a = 1
        for i in range(l,0,-1):
            cur = 0
            for j in range(len(R)):
                c = R[j][pfx[-1]+i]
                if c != ' ':
                    cur = cur * 10 + int(c)
            if b:
                a *= cur
            else:
                a += cur
        res += a
        pfx.append(col)
    print(pfx, col)
    print(res)



