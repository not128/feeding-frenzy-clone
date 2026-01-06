import math
counter=""
counter1=""
counter2=""
co=1
import tkinter as tk
root = tk.Tk()
label = tk.Label(root, text="0", font=("DejaVu Sans", 15))
label1=tk.Label(root, text='''INSTRUCTIONS: Type a number, then press enter, type another number, after that, press enter, then choose your operator.
Use the reset button to reset the calculator.''', font=("DejaVu Sans", 15))
label1.pack()
label.pack()
def a():
    global counter
    counter= str(str(counter)+"1")
    label.config(text = counter)
def b():
    global counter
    counter= str(str(counter)+"2")
    label.config(text = counter)
def c():
    global counter
    counter= str(str(counter)+"3")
    label.config(text = counter)
def d():
    global counter
    counter= str(str(counter)+"4")
    label.config(text = counter)
def e():
    global counter
    counter= str(str(counter)+"5")
    label.config(text = counter)
def f():
    global counter
    counter= str(str(counter)+"6")
    label.config(text = counter)
def g():
    global counter
    counter= str(str(counter)+"7")
    label.config(text = counter)
def h():
    global counter
    counter= str(str(counter)+"8")
    label.config(text = counter)
def i():
    global counter
    counter= str(str(counter)+"9")
    label.config(text = counter)
def j():
    global counter
    counter= str(str(counter)+"0")
    label.config(text = counter)
def k():
    global co
    global counter
    global counter2
    global counter1
    if co==1:
        counter1 = float(counter)
        counter=""
        co+=1
        label.config(text = 0)
    else:
        counter2=float(counter)
        counter=""
        co=2
        label.config(text = 0)
def l():
    global counter
    global counter1
    counter1=float(counter1)
    global counter2
    counter2=float(counter2)
    counter=counter1+counter2
    label.config(text=counter) 
    global co
    counter=str(counter)
    counter2=str(counter2)
    counter1=str(counter1)
def m():
    global counter
    global counter1
    counter1=float(counter1)
    global counter2
    counter2=float(counter2)
    counter=counter1-counter2
    label.config(text=counter) 
    counter=str(counter)
    counter2=str(counter2)
    counter1=str(counter1)
def n():
    global counter
    global counter1
    counter1=float(counter1)
    global counter2
    counter2=float(counter2)
    counter=counter1*counter2
    label.config(text=counter) 
    counter=str(counter)
    counter2=str(counter2)
    counter1=str(counter1)
def o():
    global counter
    global counter1
    counter1=float(counter1)
    global counter2
    counter2=float(counter2)
    counter=counter1/counter2
    label.config(text=counter) 
    counter=str(counter)
    counter2=str(counter2)
    counter1=str(counter1)
def p():
    global counter
    global counter1
    counter1=float(counter1)
    global counter2
    counter2=float(counter2)
    counter=counter1**counter2
    counter=str(counter)
    counter2=str(counter2)
    counter1=str(counter1)
    label.config(text=counter)
def q():
    global counter
    global counter1
    counter1=float(counter1)
    counter=math.sqrt(counter1)
    counter1=counter
    counter1=str(counter1)
    label.config(text=counter)
def r():
    global counter
    global co
    co=1    
    counter=""
    counter1=""
    counter2=""
    label.config(text=0)
def s():
    global counter
    if "." not in str(counter):
        counter= str(str(counter)+".")
        label.config(text = counter)  
def t():
    global counter
    global counter1
    counter1=float(counter1)
    counter=math.log(counter1)
    counter1=counter
    counter1=str(counter1)
    label.config(text=counter)         
def u():
    global counter
    global counter1
    counter1=float(counter1)
    counter=math.log2(counter1)
    counter1=counter
    counter1=str(counter1)
    label.config(text=counter)         
def v():
    global counter
    global counter1
    counter1=float(counter1)
    counter=math.log10(counter1)
    counter1=counter
    counter1=str(counter1)
    label.config(text=counter)         
def w():
    global counter
    global counter1
    counter1=float(counter1)
    counter=math.log1p(counter1)
    counter1=counter
    counter1=str(counter1)
    label.config(text=counter)     
def x():
    global counter
    counter=math.pi
    label.config(text=counter)
                               
button1 = tk.Button(root, text="1", font=("DejaVu Sans", 10), command=a)
button2 = tk.Button(root, text="2", font =("DejaVu Sans", 10), command=b)
button3 = tk.Button(root, text="3", font =("DejaVu Sans", 10), command=c)
button4 = tk.Button(root, text="4", font =("DejaVu Sans", 10), command=d)
button5 = tk.Button(root, text="5", font =("DejaVu Sans", 10), command=e)
button6 = tk.Button(root, text="6", font =("DejaVu Sans", 10), command=f)
button7 = tk.Button(root, text="7", font =("DejaVu Sans", 10), command=g)
button8 = tk.Button(root, text="8", font =("DejaVu Sans", 10), command=h)
button9 = tk.Button(root, text="9", font =("DejaVu Sans", 10), command=i)
button0 = tk.Button(root, text="0", font =("DejaVu Sans", 10), command=j)
buttonplus = tk.Button(root, text="+", font=("DejaVu Sans", 10), command=l)
buttonminus = tk.Button(root, text="-", font=("DejaVu Sans", 10), command=m)
buttontimes = tk.Button(root, text="*", font=("DejaVu Sans", 10), command=n)
buttondivide = tk.Button(root, text="/", font=("DejaVu Sans", 10), command=o)
buttonpower = tk.Button(root, text="^", font=("DejaVu Sans", 10), command=p)
buttonsqrt = tk.Button(root, text="√", font=("DejaVu Sans", 10), command=q)
buttonreset = tk.Button(root, text="Reset", font=("DejaVu Sans", 10), command=r)
buttonenter=tk.Button(root, text="Enter", font=("DejaVu Sans", 10), command=k)
buttondec=tk.Button(root, text=".", font=("DejaVu Sans", 10), command=s)
buttonlog = tk.Button(root, text="ln", font=("DejaVu Sans", 10), command=t)
buttonlog2 = tk.Button(root, text="log₂", font=("DejaVu Sans", 10), command=u)
buttonlog10=tk.Button(root, text="log\u2081\u2080", font=("DejaVu Sans", 10), command=v)
buttonlog1p=tk.Button(root, text="log1p", font=("DejaVu Sans", 10), command=w)
buttonpi=tk.Button(root, text="π", font=("DejaVu Sans", 10), command=x)
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button0.pack() 
buttondec.pack()
buttonplus.pack() 
buttonminus.pack()
buttontimes.pack()
buttondivide.pack()
buttonpower.pack()
buttonpi.pack()
buttonsqrt.pack()
buttonlog.pack()
buttonlog10.pack()
buttonlog2.pack()
buttonlog1p.pack()     
buttonenter.pack()
buttonreset.pack()
root.mainloop()
