file = "in2.txt"
with open(file, "r") as txt:
    R = []
    for line in txt.readlines():
        s = line.strip()
        if s[0] in '*+':
            s = s.split()
            d = [0] * len(R[0])
            for i in range(len(R[0])):
                if s[i] == '*':
                    d[i] = 1
                print(s[i])
                for j in range(len(R)):
                    if s[i] == '*':
                        d[i] *= R[j][i]
                    else:
                        d[i] += R[j][i]
            print(sum(d))
        else:
            A = list(map(int, s.split()))
            R.append(A)

