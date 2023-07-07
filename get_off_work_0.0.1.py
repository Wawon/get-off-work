
# 导入需要的库
from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox

# 创建窗口
window = Tk()
window.title("下班倒计时")
window.geometry("560x112-500-500")

# 创建透明色背景用
A = ttk.Style()
A.theme_use('winnative')
A.configure("my0.Horizontal.TProgressbar", troughcolor='white', darkcolor='white', lightcolor='white',
            bordercolor='white', background='green', thickness=10)

"""窗口内容"""
# 第0行主要内容（不含按钮） 行是row
lbl1 = Label(window, text="请在右侧输入上班的时间（24小时制）", font=("等线", 12))
lbl1.grid(column=0, row=0)
sbh = Spinbox(window, from_=0, to=23, width=5)
sbh.grid(column=1, row=0)
lbl2 = Label(window, text="时", font=("等线", 12), height=1, width=4, anchor="center")
lbl2.grid(column=2, row=0, sticky=W)
sbm = Spinbox(window, from_=0, to=59, width=5)
sbm.grid(column=3, row=0)
lbl3 = Label(window, text="分", font=("等线", 12), height=1, width=4, anchor="center")
lbl3.grid(column=4, row=0, sticky=W)

# 第1行主要内容（不含按钮） 行是row
lbl4 = Label(window, text="请在右侧输入午休的时间（24小时制）", font=("等线", 12))
lbl4.grid(column=0, row=1)
wxh = Spinbox(window, from_=0, to=23, width=5)
wxh.grid(column=1, row=1)
lbl5 = Label(window, text="时", font=("等线", 12), height=1, width=4, anchor="center")
lbl5.grid(column=2, row=1, sticky=W)
wxm = Spinbox(window, from_=0, to=59, width=5)
wxm.grid(column=3, row=1)
lbl6 = Label(window, text="分", font=("等线", 12), height=1, width=4, anchor="center")
lbl6.grid(column=4, row=1, sticky=W)

# 第2行主要内容（不含按钮） 行是row
lbl7 = Label(window, text="请在右侧输入下班的时间（24小时制）", font=("等线", 12))
lbl7.grid(column=0, row=2)
xbh = Spinbox(window, from_=0, to=23, width=5)
xbh.grid(column=1, row=2)
lbl8 = Label(window, text="时", font=("等线", 12), height=1, width=4, anchor="center")
lbl8.grid(column=2, row=2, sticky=W)
xbm = Spinbox(window, from_=0, to=59, width=5)
xbm.grid(column=3, row=2)
lbl9 = Label(window, text="分", font=("等线", 12), height=1, width=4, anchor="center")
lbl9.grid(column=4, row=2, sticky=W)


# 被调用的函数，层级-3
def time_remaining(target_hour, target_min):
    t = time.localtime()
    hours_remaining = target_hour - t.tm_hour - (1 if target_min <= t.tm_min else 0)
    minutes_remaining = target_min - t.tm_min if target_min > t.tm_min else 59 - t.tm_min + target_min
    seconds_remaining = 60 - t.tm_sec
    return hours_remaining, minutes_remaining, seconds_remaining


def bar_percent(start_hour, start_min, end_hour, end_min):
    t = time.localtime()
    hours_1 = end_hour - start_hour - (1 if end_min <= start_min else 0)
    minutes_1 = end_min - start_min if end_min > start_min else 59 - start_min + end_min
    totall_minutes = int(hours_1)*60 + int(minutes_1)
    hours_2 = t.tm_hour - start_hour - (1 if t.tm_min <= start_min else 0)
    minutes_2 = t.tm_min - start_min if t.tm_min > start_min else 59 - start_min + t.tm_min
    already_minutes = int(hours_2)*60 + int(minutes_2)
    p = already_minutes * 100 / totall_minutes
    return p


# 被调用的函数，层级-2
def timing():

    lbl10.configure(text=f"现在是北京时间 {time.strftime('%H 点 %M 分 %S 秒')}",
                    font=("等线", 12, "bold"), bg='white', height=1, width=30, anchor="center")


def nap_count():
    a_h, a_m, a_s = time_remaining(int(wxh.get()), int(wxm.get()))
    lbl11.configure(text=f"距离午休时间还有 {a_h}小时 {a_m}分 {a_s}秒", font=("等线", 12, "bold"), bg='white', height=1, width=30,
                    anchor="center")


def lunch_break():
    messagebox.showwarning(title='午休了', message='干饭时间到！')


def off_count():
    h_remain, m_remain, s_remain = time_remaining(int(xbh.get()), int(xbm.get()))
    lbl12.configure(text=f"距离下班还有 {h_remain} 小时 {m_remain} 分 {s_remain} 秒", font=("等线", 12, "bold"), bg='white', height=1, width=30,
                    anchor="center")


def get_off_work():
    messagebox.showwarning(title='下班了', message='我警告你，下班了！')


def off_work():
    lbl12.configure(text=f"下班了还不跑？", font=("等线", 12), height=1, width=30, anchor="w")


def show_progressbar():
    t = time.localtime()
    ap = bar_percent(int(sbh.get()), int(sbm.get()), int(xbh.get()), int(xbm.get()))
    progressbar_1 = ttk.Progressbar(window, style="my0.Horizontal.TProgressbar", length=300)
    progressbar_1.grid(row=7, column=0, sticky=N)
    progressbar_1['maximum'] = 100
    progressbar_1['value'] = ap
    if (t.tm_hour == int(xbh.get()) and t.tm_min >= int(xbm.get())) or t.tm_hour > int(xbh.get()):
        progressbar_1.grid_forget()
    window.update()


# 第1页面的按钮对应的功能需要用的函数 层级-1
def time_rule():
    t = time.localtime()
    if t.tm_hour < int(wxh.get()) or (t.tm_hour == int(wxh.get()) and t.tm_min < int(wxm.get())):
        timing()
        nap_count()
    if t.tm_hour == int(wxh.get()) and t.tm_min == int(wxm.get()) and t.tm_sec < 3:
        lunch_break()
    if (t.tm_hour == int(wxh.get()) and t.tm_min >= int(wxm.get())) or t.tm_hour > int(wxh.get()):
        timing()
        lbl11.grid_forget()

    if t.tm_hour < int(xbh.get()) or (t.tm_hour == int(xbh.get()) and t.tm_min < int(xbm.get())):
        timing()
        off_count()
        show_progressbar()
    if t.tm_hour == int(xbh.get()) and t.tm_min == int(xbm.get()) and t.tm_sec < 2:
        get_off_work()
        show_progressbar()
    if (t.tm_hour == int(xbh.get()) and t.tm_min >= int(xbm.get())) or t.tm_hour > int(xbh.get()):
        off_work()


# 第1页面的按钮对应的功能 层级0
def save_default():
    with open('default_values.txt', 'w') as f:
        f.write(f'{sbh.get()}\n{sbm.get()}\n{wxh.get()}\n{wxm.get()}\n{xbh.get()}\n{xbm.get()}')


def read_default():
    try:
        with open('default_values.txt', 'r') as f:
            values = f.readlines()
            sbh.delete(0, END)
            sbh.insert(0, values[0].strip())
            sbm.delete(0, END)
            sbm.insert(0, values[1].strip())
            wxh.delete(0, END)
            wxh.insert(0, values[2].strip())
            wxm.delete(0, END)
            wxm.insert(0, values[3].strip())
            xbh.delete(0, END)
            xbh.insert(0, values[4].strip())
            xbm.delete(0, END)
            xbm.insert(0, values[5].strip())
    except FileNotFoundError:
        pass


def start():
    t = time.localtime()
    sbh.grid_forget()
    sbm.grid_forget()
    wxh.grid_forget()
    wxm.grid_forget()
    xbh.grid_forget()
    xbm.grid_forget()

    lbl1.grid_forget()
    lbl2.grid_forget()
    lbl3.grid_forget()
    lbl4.grid_forget()
    lbl5.grid_forget()
    lbl6.grid_forget()
    lbl7.grid_forget()
    lbl8.grid_forget()
    lbl9.grid_forget()

    save.grid_forget()
    read.grid_forget()
    start.grid_forget()
    if (t.tm_hour == int(wxh.get()) and t.tm_min >= int(wxm.get())) or t.tm_hour > int(wxh.get()):
        window.geometry('300x59-1-33')
    else:
        window.geometry('300x89-1-33')
    window.attributes('-alpha', 0.5)
    window.title(" ")
    window.config(bg='white')
    window.wm_attributes('-transparentcolor', 'white')

    def update_time():
        time_rule()
        window.after(1000, update_time)

    update_time()


# 第一页面的按钮
save = Button(window, text="保存数字", font=("等线", 12), command=save_default,
              height=1, width=9, anchor="center", )
save.grid(column=5, row=1, pady=3, sticky=W)

read = Button(window, text="读取存档", font=("等线", 12), command=read_default,
              height=1, width=9, anchor="center")
read.grid(column=5, row=0, pady=3, sticky=W)

start = Button(window, text="开始等下班", font=("等线", 12), command=start,
               height=1, width=9, anchor="center")
start.grid(column=5, row=2, pady=3, sticky=W)

# 第一页面的4个空位
lbl10 = Label(window, text=" ")
lbl10.grid(column=0, row=4)
lbl11 = Label(window, text=" ")
lbl11.grid(column=0, row=5)
lbl12 = Label(window, text=" ")
lbl12.grid(column=0, row=6)

# 调整窗口位置并显示窗口
window.wm_attributes('-topmost', 1)
window.mainloop()
