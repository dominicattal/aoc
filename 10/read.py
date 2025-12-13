file = "in1.txt"
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
        print(len(buttons), end=" ")
        for i in range(len(buttons)):
            mask = 0
            for j in buttons[i]:
                mask |= 1<<(len(joltages)-1)
            print(mask, end=" ")
        print(len(target), end=" ")
        for t in target:
            print(t, end=" ")
        print(buttons, target)
    print(res)

# solutions for testcase
# (1,3,0,3,1,2) 10
# (2,5,0,5,0) 12
# (5,0,5,1) 11
