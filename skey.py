'''
@描述: 
@作者: 李天红
@Github: https://github.com/Celint/cryptography
@Date: 2019-06-11
'''
import tkinter as tk
import tkinter.messagebox 
import hashlib as hs
import os
# 实例化窗口
window = tk.Tk()
window.title("skey身份鉴别")
window.geometry('500x700')
var = tk.StringVar()
var.set('你好！欢迎使用身份鉴别协议')
l = tk.Label(window, bg='red', font=('Microsoft YaHei', 12), width=30, height=2, textvariable=var)
l.pack()
canvas = tk.Canvas(window, bg='white', height=600, width=500)
image_file = tk.PhotoImage(file='pig.gif')
image = canvas.create_image(250, 0, anchor='n', image=image_file)
# canvas.pack()
l1 = tk.Label(window, text='用户名')
l1.pack()
e = tk.Entry(window, show=None)
e.pack()
l2 = tk.Label(window, text='密码')
l2.pack()
ep = tk.Entry(window, show='*')
ep.pack()

def ret():
    var.set('你好！欢迎使用身份鉴别协议')
    canvas.forget()
    l1.pack()
    e.pack()
    l2.pack()
    ep.pack()
    btn.pack()
    btr.pack()

btrr = tk.Button(window, text="退出", width=15, height=2, command=ret)

def login():
    val1 = e.get()
    val2 = ep.get()
    if os.path.exists('keys/' + val1 + ".txt") == True:
        f = open('keys/' + val1 + ".txt", 'r')
        lines = []
        while True:
            line = f.readline()
            if not line:
                break
            lines.append(line)
        md = hs.md5()
        md.update(val2.encode())
        if md.hexdigest() == lines[-1][:-1]:
            f = open('keys/' + val1 + ".txt", 'w')
            f.write('')
            f = open('keys/' + val1 + ".txt", 'a')
            for i in range(0, len(lines) - 1):
                f.write(lines[i])
            var.set('登录成功!')
            btrr.pack()
            canvas.pack()
            l1.forget()
            e.forget()
            l2.forget()
            ep.forget()
            btn.forget()
            btr.forget()
        else:
            var.set('密码错误，请重新登录！')
    else:
        tk.messagebox.askokcancel(title="提示", message="不存在此用户")
    

def regist():
    reg = tk.Toplevel(window)
    reg.title('注册')
    reg.geometry('300x250')
    e1 = tk.Entry(reg, show=None)
    e1.pack()
    def regi():
        r = e1.get()
        if os.path.exists('keys/' + r + ".txt") == False:
            f = open("keys/" + r + ".txt", 'a')
            md = hs.md5()
            md.update(r.encode())
            f.write(md.hexdigest() + '\n')
            for i in range(0, 99):
                r = md.hexdigest()
                md = hs.md5() # 重新实例化，防止覆盖
                md.update(r.encode())
                f.write(md.hexdigest() + '\n')
            tk.messagebox.askokcancel(title="提示", message="注册成功")
        else:
            tk.messagebox.askokcancel(title="提示", message="该用户已被注册")

    btre = tk.Button(reg, text="注册", width=15, height=2, command=regi)
    btre.pack()

btn = tk.Button(window, text='登录', width=15, height=2, command=login)
btn.pack()

btr = tk.Button(window, text='去注册', width=15, height=2, command=regist)
btr.pack()

window.mainloop()