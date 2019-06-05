'''
@描述: 列移位密码
@作者: 李天红
@Github: https://github.com/Celint/cryptography
@Date: 2019-06-05
'''
f = open("Book3.txt", "r")
str = f.read()
f.close()
r = []
leng = []
for i in range(2, 13):
    if len(str) % i == 0:
        length = int(len(str) / i)
        r.append(i)
        leng.append(length)
li = []
for i in range(0, len(r)):
    for j in range(0, r[i]):
        li.append(str[j * leng[i]:(j + 1) * leng[i]])
    for j in range(0, len(li[0])):
        for k in range(0, len(li)):
            print(li[k][j], end='')
    print('\n')
    li = []
