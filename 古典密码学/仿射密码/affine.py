f = open("Book2.txt", "r")
Cs = f.read()
f.close()
txt = "abcdefghijklmnopqrstuvwxyz .,"
# 求乘法逆元


def getGcd(a, b):
    if b == 0:
        return 1, 0
    else:
        k = int(a / b)
        r = a % b
        x1, y1 = getGcd(b, r)
        x, y = y1, x1 - k * y1
        return x, y


# 求2~28的乘法逆元 mod 29
k = []
for i in range(2, 28):
    x, y = getGcd(i, 29)
    k.append(x % 29)
# k.insert(0, 0)
with open("b.txt", 'a') as t:
    for a in k:
        for b in range(0, 29):
            for c in Cs:
                if c in txt:
                    if c == ' ':
                        t.write(txt[(a * (123 - b)) % 29])
                    elif c == '.':
                        t.write(txt[(a * (124 - b)) % 29])
                    elif c == ',':
                        t.write(txt[(a * (125 - b)) % 29])
                    else:
                        t.write(txt[(a * (ord(c) - b)) % 29])
                else:
                    t.write(c)
            t.write('\n\n')
