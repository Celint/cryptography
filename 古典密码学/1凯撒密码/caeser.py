f = open("Book1.txt", "r")
str = f.read()
f.close()
# for ch in str:
#     print(ch, end = '')  
# 将字符转ASCII码，再移位，将移位后的ASCII码转换为字符         
# a = 'c';
# print(chr(ord(a) + 2))
# z和Z的ASCII码
# print(ord('z'), ord('Z'), ord('a'), ord('A'))
# 122 90 97 65
for i in range(0, 26):
        for ch in str:
                if ord(ch) in range(65, 91):
                        if ord(ch) + i in range(65, 91):
                                print(chr(ord(ch) + i), end = '')
                        else:
                                print(chr(ord(ch) + i - 26), end = '')
                elif ord(ch) in range(97, 123):
                        if ord(ch) + i in range(97, 123):
                                print(chr(ord(ch) + i), end = '')
                        else:
                                print(chr(ord(ch) + i - 26), end = '')
                else:
                        print(ch, end = '')
        print('\n')