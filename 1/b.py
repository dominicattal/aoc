x = 50
cnt = 0
with open("inp2.txt","r") as txt:
    for line in txt:
        s = line.strip()
        k = int(s[1:])
        if s[0] == 'L':
            x -= k
        else:
            x += k
        cnt += abs(x//100)
        x %= 100
print(cnt)