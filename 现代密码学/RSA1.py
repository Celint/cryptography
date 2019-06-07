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

n = 11395221282616778531

e = 65537

c = 3216222868678880564

gen = int(pow(n, 1 / 2))
if gen % 2 == 1:
    x, y = gen, gen + 2
else:
    x, y = gen - 1, gen + 1
while x * y != n:
    if x * y > n:
        x -= 2
    else:
        y += 2
print("p = ", x, ", q = ", y)
fn = (x - 1) * (y - 1)
x, y = getGcd(e, fn)
re = x % fn
d = re % fn
m = pow(c, d, n)
print("fn =", fn, "re =", re, "d =", d, "m =", m)