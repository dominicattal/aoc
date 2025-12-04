s = input()
res = 0
lst = s.split(',')
for l in lst:
    l, r = l.split('-')
    l = int(l)
    r = int(r)
    for k in range(l,r+1):
        qq = str(k)
        for i in range(len(qq)-1):
            if len(qq) % (i+1) != 0: continue
            p = qq[:i+1] * (len(qq) // (i+1))
            if p == qq:
                res += k
                break
print(res)  