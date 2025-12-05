inp = "in2.txt"
with open(inp, "r") as txt:
    A = []
    B = []
    f = True
    for line in txt.readlines():
        s = line.strip()
        if s == '':
            f = False
            continue
        if f:
            l, r = map(int, s.split('-'))
            A.append((l,r))
        else:
            B.append(int(s))
    res = 0
    for n in B:
        for l,r in A:
            if l <= n <= r:
                break
        else:
            res += 1
    print(len(B)-res)
