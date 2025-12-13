file = "in2.txt"
with open(file, "r") as txt:
    res = 0
    for line in txt.readlines():
        s = line.strip()
        S = s.split()
        light = S[0]
        n = len(light)-2
        t = 0
        for i in range(1, len(light)-1):
            b = 1 if light[i] == '#' else 0
            t = t + (b<<(i-1))
        masks = []
        for i in range(1, len(S)-1):
            bits = list(map(int, S[i][1:-1].split(',')))
            m = 0
            for b in bits:
                m |= 1<<b
            masks.append(m)
        ret = 100
        for i in range(1<<len(masks)):
            cur = 0
            for j in range(len(masks)):
                if (i>>j)&1:
                    cur ^= masks[j]
            if cur == t:
                ret = min(ret, i.bit_count())
        res += ret
    print(res)

