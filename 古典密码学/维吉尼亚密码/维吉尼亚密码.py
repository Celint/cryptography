'''
@描述: 破解维吉尼亚密码
@作者: 兰彬炎
@Github: https://github.com/Celint/cryptography
@Date: 2019-06-28
'''
import math
import gmpy2
def get_key_length(cipher): #猜密钥长度，分组计算平均重合指数
   for step in range(2,13):
        IC = 0.0
        matrix = divide(cipher,step)     #分组
        print("假设秘钥长度为：")
        print(step)
        for i in range(0,step):
            w = [row[i]  for  row in matrix] #这是我要判断的那一个组了
            ls=[]
            ls = count_list(w)
            total = 0.0
            for j in range (0,26):
                total += ls[j]*(ls[j]-1)/(len(w)*len(w)-1)
            IC+=total        
        print("  平均重合指数为：" )
        print(IC/step)
def count_list(ttt):        #统计数组ttt中英文字母的个数
    ls = []
    for m in range(0,26):
        ls.append(0)
    for j in ttt:
        if  0<=ord(j)-97<26:
            ls[ord(j)-97]+=1
        elif 0<=ord(j)-65<26:
            ls[ord(j)-65]+=1
    return ls
def guess_key(cipher,keylength):    #获取每一组的秘钥，凯撒密码
    alphaRate =[0.08167,0.01492,0.02782,0.04253,0.12705,0.02228,0.02015,0.06094,0.06996,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.0009,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.0015,0.01974,0.00074]
    key = []#保存秘钥
    #用keylength对密文分组，
    matrix = divide(cipher,keylength)
    #然后每一组凯撒密码计算重合指数
    for i in range(0,keylength):
        w = [row[i]  for  row in matrix] #这是我要判断的那一个组了
        ls = count_list(w)
        IC =[]  #记录26个不同秘钥时对应的重合指数
        for k in range(0,26):                      
            sum = 0.0
            for m in range(0,26):
                sum+=alphaRate[m]*ls[m] / len(w)
            IC.append(sum)
            ls = ls[1:]+ls[:1]  #移位表示秘钥加了1时对应的一个临时明文
        num =100
        sign = -1
        for i in range(0,26):
            if  abs(IC[i]-0.065546)<num:
                num =abs(IC[i]-0.065546)
                sign = i
        key.append(sign)
    return key      
def divide(cipher,keylength):  #返回一个二维数组，以便于分组统计
    matrix = []
    row=[]
    index =0
    for ch in cipher:
        row.append(ch)
        index+=1
        if  index %keylength==0:
            matrix.append(row)
            row=[ ]
    return matrix
f = open("Book4.txt", "r")
cipher = f.read()
f.close()
origin = []
get_key_length(cipher)
keylength = eval(input("你觉得秘钥长度是："))
key = []
key =guess_key(cipher,keylength)
count = 0
for  ch in cipher:
    if   ord('a')<=ord(ch)<=ord('z'):
        origin.append(    chr(       (ord(ch)-ord('a')-key[count])    %26 + ord('a')     ))
    elif  ord('A')<=ord(ch)<=ord('Z'):
        origin.append(   chr(       (ord(ch)-ord('A')-key[count])    %26 + ord('A')     ))
    else :
        origin.append(ch)
    count+=1
    count %= keylength
text=""
key_str = ""
for ch in origin:
    text+=ch
for i in key:
    key_str+=chr(i+97)
print(key_str)
print(text)