with open("in2.txt", "r") as txt:
    res = 0
    for line in txt.readlines():
        s = line.strip()
        cur = 0
        for i in range(len(s)):
            for j in range(i):
                t = int(s[j]+s[i])
                cur = max(cur, int(t))
        res += cur
    print(res)

