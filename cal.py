from tkinter import *
root=Tk()
root.title("calculator")
root.resizable(1,1)
root.wm_attributes("-topmost",1)
 
Label1=Label(root,text="calculator")
Label1.grid(row=0,columnspan=8)

expression=""
equation=StringVar()
calculation=Label(root,textvariable=equation)
equation.set("enter expression")
calculation.grid(row=2,columnspan=8)

def Press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def equal():
    global expression
    total=str(eval(expression))
    equation.set(total)
    expression=""
def clear():
    global expression
    expression=""
    equation.set("")
    
button1=Button(root,text="1" , command=lambda:Press(1),borderwidth=1)
button1.grid(row=6,column=2,padx=10,pady=10)
button2=Button(root,text="2" , command=lambda:Press(2),borderwidth=1)
button2.grid(row=3,column=1,padx=10,pady=10)
button3=Button(root,text="3" , command=lambda:Press(3),borderwidth=1)
button3.grid(row=3,column=2,padx=10,pady=10)
button4=Button(root,text="+" , command=lambda:Press("+"),borderwidth=1)
button4.grid(row=3,column=3,padx=10,pady=10)
button5=Button(root,text="4" , command=lambda:Press(4),borderwidth=1)
button5.grid(row=4,column=1,padx=10,pady=10)
button6=Button(root,text="5" , command=lambda:Press(5),borderwidth=1)
button6.grid(row=4,column=2,padx=10,pady=10)
button7=Button(root,text="6" , command=lambda:Press(6),borderwidth=1)
button7.grid(row=4,column=3,padx=10,pady=10)
button8=Button(root,text="-" , command=lambda:Press("-"),borderwidth=1)
button8.grid(row=5,column=1,padx=10,pady=10)
button9=Button(root,text="7" , command=lambda:Press(7),borderwidth=1)
button9.grid(row=5,column=2,padx=10,pady=10)
a=Button(root,text="8" , command=lambda:Press(8),borderwidth=1)
a.grid(row=5,column=3,padx=10,pady=10)
b=Button(root,text="9" , command=lambda:Press(9),borderwidth=1)
b.grid(row=3,column=4,padx=10,pady=10)
c=Button(root,text="*" , command=lambda:Press("*"),borderwidth=1)
c.grid(row=4,column=4,padx=10,pady=10)
d=Button(root,text="0" , command=lambda:Press(0),borderwidth=1)
d.grid(row=5,column=4,padx=10,pady=10)
e=Button(root,text="=" , command=lambda:equal(),borderwidth=1)
e.grid(row=6,column=4,padx=10,pady=10)
f=Button(root,text="/" , command=lambda:Press("/"),borderwidth=1)
f.grid(row=6,column=3,padx=10,pady=10)
g=Button(root,text="C" , command=lambda:clear(),borderwidth=1)
g.grid(row=6,column=1,padx=10,pady=10)

root.mainloop()

