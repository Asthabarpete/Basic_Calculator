from tkinter import *
root=Tk()
root.title("BASIC CALCULATOR")
root["bg"] = "lightslategray"
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(num):
    curr=e.get()
    e.delete(0,END)
    e.insert(0,str(curr)+str(num))
def b_clear():
    e.delete(0, END)
def b_add():
    firstNumber=e.get()
    global f_num
    global calculation
    calculation="ADD"
    f_num=int(firstNumber)
    button_click("+")
    #e.delete(0,END)

def b_sub():
    firstNumber = e.get()
    global f_num
    global calculation
    calculation = "SUB"
    f_num = int(firstNumber)
    button_click("-")
    #e.delete(0, END)
def b_mul():
    firstNumber = e.get()
    global f_num
    global calculation
    calculation = "MUL"
    f_num = int(firstNumber)
    button_click("*")
    #e.delete(0, END)
def b_div():
    firstNumber = e.get()
    global f_num
    global calculation
    calculation = "DIV"
    f_num = int(firstNumber)
    button_click("/")
    #e.delete(0, END)
def b_mod():
    firstNumber = e.get()
    global f_num
    global calculation
    calculation = "MOD"
    f_num = int(firstNumber)
    button_click("%")
    #e.delete(0, END)
def b_equal():
    secondNumber=e.get()
    e.delete(0,END)
    if calculation=="ADD":
        i=secondNumber.index('+')
        s_num=secondNumber[(i+1):]
        e.insert(0,f_num + int(s_num))
    if calculation=="SUB":
        i = secondNumber.index('-')
        s_num = secondNumber[(i + 1):]
        e.insert(0,f_num - int(s_num))
    if calculation=="DIV":
        i = secondNumber.index('/')
        s_num = secondNumber[(i + 1):]
        e.insert(0,f_num / int(s_num))
    if calculation=="MUL":
        i = secondNumber.index('*')
        s_num = secondNumber[(i + 1):]
        e.insert(0,f_num * int(s_num))
    if calculation=="MOD":
        i = secondNumber.index('%')
        s_num = secondNumber[(i + 1):]
        e.insert(0,f_num % int(s_num))

button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
button_sum = Button(root,text="+",padx=40,pady=20,command=b_add)
button_sub = Button(root,text="- ",padx=40,pady=20,command=b_sub)
button_mul= Button(root,text="* ",padx=40,pady=20,command=b_mul)
button_div = Button(root,text="/ ",padx=40,pady=20,command=b_div)
button_mod = Button(root,text="%",padx=40,pady=20,command=b_mod)
button_equal = Button(root,text="=",padx=40,pady=20,command=b_equal)
button_clear = Button(root,text="clear",padx=90,pady=20,command=b_clear)

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_sum.grid(row=4,column=1)
button_sub.grid(row=4,column=2)
button_mul.grid(row=5,column=0)
button_div.grid(row=5,column=1)
button_mod.grid(row=5,column=2)
button_equal.grid(row=6,column=0)
button_clear.grid(row=6,column=1,columnspan=2)

root.mainloop()
