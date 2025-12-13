from random import randint
from math import exp
from bisect import bisect_left
file = "in2.txt"
with open(file, "r") as txt:
    res = 0
    for line in txt.readlines():
        s = line.strip()
        S = s.split()
        buttons = []
        for i in range(1, len(S)-1):
            button = tuple(map(int, S[i][1:-1].split(',')))
            buttons.append(button)
        target = tuple(map(int,S[-1][1:-1].split(',')))
        n = len(buttons)
        m = len(target)
        pfx = [0] * (n+1)
        for i in range(1,len(pfx)):
            pfx[i] = pfx[i-1] + len(buttons[i-1])
        mat = [[0] * m for _ in range(n)]
        joltage_sums = [0] * m
        for i, button in enumerate(buttons):
            for joltage in button:
                mat[i][joltage] = 1
                joltage_sums[joltage] += 1
        def mul(vec):
            out = [0] * len(mat[0])
            for i in range(len(mat[0])):
                for j in range(len(vec)):
                    out[i] += mat[j][i]*vec[j]
            return tuple(out)
        def rand_button():
            r = randint(0,pfx[n-1])
            return bisect_left(pfx[:-1], r)
        cur = [0] * n
        kmax = 10**5
        k = 0
        best = [10**9, tuple(cur)]
        cur_sum = 0
        # first, find a solution. other solutions should be aruond there
        # give it about kmax iterations. if a better solution isnt found, probably
        # the right answer. otherwise, reset the counter and go from the new sol
        while k < kmax or best[0] == 10**9:
            k += 1
            i = rand_button()
            tot_add = tot_sub = 10**9
            if cur[i] > 0:
                cur[i] -= 1
                out_sub = mul(cur)
                diff_sub = [abs(target[i]-out_sub[i]) for i in range(m)]
                tot_sub = sum(diff_sub)
                cur[i] += 1
            if cur_sum < best[0]:
                cur[i] += 1
                out_add = mul(cur)
                diff_add = [abs(target[i]-out_add[i]) for i in range(m)]
                tot_add = sum(diff_add)
                cur[i] -= 1
            if tot_add == tot_sub == 10**9:
                continue
            elif tot_add < tot_sub:
                cur[i] += 1
                cur_sum += 1
            elif cur[i] > 0:
                cur[i] -= 1
                cur_sum -= 1
            if cur_sum < best[0] and mul(cur) == target:
                best = [cur_sum, tuple(cur)]
                k = 0
        print(best)
        res += best[0]
    print(res)

# solutions for testcase
# (1,3,0,3,1,2) 10
# (2,5,0,5,0) 12
# (5,0,5,1) 11
# 20351
