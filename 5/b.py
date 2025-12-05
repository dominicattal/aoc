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
    R = []
    for l, r in A:
        for i in range(len(R)):
            if R[i][0] <= l <= R[i][1] or R[i][0] <= r <= R[i][1]:
                R[i][0] = min(R[i][0],l)
                R[i][1] = max(R[i][1],r)
                break
        else:
            R.append([l,r])
        i = j = 0
        while i < len(R):
            j = 0
            while j < i:
                l1,r1 = R[i]
                l2,r2 = R[j]
                if l1 <= l2 <= r1 or l1 <= r2 <= r1:
                    R[i][0] = min(l1,l2)
                    R[i][1] = max(r1,r2)
                    R.pop(j)
                    i = 0
                    break
                j += 1
            else:
                i += 1


    for l, r in R:
        res += r-l+1
    print(res)
