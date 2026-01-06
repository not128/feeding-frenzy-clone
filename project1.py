# # import time
# # import turtle

# # list12 = []
# # his_name = "john" # string
# # list1 = ["place0", "place1", "place2", "place3", "place4"]
# # age =  19 # integer
# # ford = "hello" 
# # a_number = 12345
# # number1, number2, number3 = 1, 2, 3
# # print(ford + " " + his_name + " is"+" "+ str(age) +" years old", int(age))
# # print(number1, number2, "example 1")
# # age = 20
# # print(ford + " " + his_name + " is"+" "+ str(age) +" years old")
# # print(number1, number2, "example 2")
# # for i in range(5):
# #  if not number2*number3==5 or number1+number2==4:
# #   print("yes number2 times number3 equals 6 or number1 plus number2 is 3")
# #  else:
# #   print ('''maybe I am wrong
# #          **
# #          ***
# #          ****
# #          *****''')   
# #  print("goodbye")
# # print(ford[len(ford)-1])
# # if "hello" not in ford:
# #   print("a")
# # abc=int(input())
# # if abc <= 4 and abc >= 0:
# #  print(list[abc])
# # else:
# #  print("The list was not printed because the value you entered was not in the list's limits(0-4)")     
# # t = turtle.Turtle()
# # turtle.colormode(255)
# # t.pencolor(51, 177, 250)
# # t.fillcolor(46, 95, 255)
# # t.penup()
# # t.pensize(10)
# # t.speed(2)
# # t.goto(x=110, y=0.0)
# # t.pendown()
# # t.begin_fill()
# # t.seth(180)
# # time.sleep(1.5)
# # t.end_fill()
# # t.setheading(180)
# # time.sleep(5)
# # print(t)
# # print("what does that mean?")
# # list12.add("hello")
# # print(list12)
# # turtle.done()

# # ////////////////////////////////////30/09/2025
# list12 = []
# list12.append("hello, world!") 
# print(list12)   
# abc = list12 
# print(abc)
# list12.append("hello")
# print(list12)
# tuple1 = ("abc", "abc")
# print(tuple1)
# set2 = {"hel2lo", "hello"}
# print(set2)
# a=1
# dictionary_ = {
#   "2003_ford_windstar":"has a v6",
#   "my_favorite_car": "yes one time, but no"
# }
# for i in set2:
#   a = a+1
#   print(i)
# for i, y in dictionary_.items():
#   print(i, y)
# if "hel2lo" in set2:
#   print("yes")
# else:
#   print("no")
# a=6  
# print("elif")
# i = 54321
# while a>5:
#   set2 = i
# print(set2)
  
  
# function : block

# initial function
# def My_function():
#   pass

# # not return and not Reference
# def Print_value():
#   print("hahaha")
  
# Print_value() ## call function

# # have return and not Ref
# def My_age():
#   print("hello Trung Nguyen")
#   age = 8
#   return age

# age_trungNguyen = My_age()
# print(age_trungNguyen)

# # not return and have ref

# def Calculate_sum(number1, number2):
#   sum_numbers = number1 + number2
#   print(sum_numbers)
  
# Calculate_sum([1,2,3],[4,5,6])

# # have return and ref
# def Calculate_sum2(number1, number2):
#   sum_numbers1 = number1 + number2
#   return sum_numbers1
# mysum = Calculate_sum2(5, 10)

# print(mysum)
# n = int(input("ask me"))
# def Calc_sum(n):
#   ab = n
#   while ab > 1 :
#     ab = ab-1
#     n = n+ab
#     print(n)
# Calc_sum(n)
# def multiplication(a, b):
#   return(a * b)
# multiplication1 = multiplication(int(input("int, please! ")),int(input("int, please! ")))
# print(multiplication1)
# class Class1:
#   def __init__(self, age, name, CCCD):
#     self.age = age
#     self.name = name
#     self.CCCD = CCCD
  
#   def chamconglam(self):
#     print("Cham cong ngay !")
  
#   def chamcongnghi(self):
#     print("Cham cong nghi, khong co luong.")
    
    
# class employee(Class1):
#   def __init__(self, kinhnghiem, trinhdo, id):
#     self.kinhnghiem = kinhnghiem
#     self.trinhdo = trinhdo
#     self.id = id
  
#   def in_thong_tin(self):
#     print(f"Tên: {self.name}, Tuổi: {self.age}, CCCD: {self.CCCD}, Tuổi: {self.age}, Kinh nghiệm: {self.kinhnghiem}, Trình độ: {self.trinhdo}")

# baove = Class1("nguyen", 9, "CCCD114245")
# ketoan = Class1("Nhi", 15, "CCCD152545")
# baove.chamconglam()
# ketoan.chamcongnghi()
# baove1 = employee()


# # % : 9 % 2 = 1
# # //: 11//2 = 5  ------ 5.4444444444
# a = ["a", "b"]
# a.remove()
# a.append("hello, world!")
# a[0]
# def exanplme(a):
#   pass

# def x(a,b):
#   print(a+b)

# x(5,6)
# x = lambda a,b : a+b
# print(x(5,6))

# j = 5
# global o 
# o = j
# a = 0
# num = int(input())
# length = 0
# lista = []
# for i in range (num):
#   a = a + 1
#   lista.append(a)
#   print(lista)

# n = 10
# number = 0
# number1 = 1
# for i in range(n):
  
#   number1 = number + number1
#   number = number1-number
#   print(number, end = ' ')
  
# n = int(input())
# x = 0
# for i in range(n):
#   value = input()
#   if "+" in value:
#     x+=1
#   if "-" in value:
#     x-=1
# print(x)  

# def sum1(n):
#   if n == 1:
#     return 1
#   return sum1(n-1)+n   
# print(sum1(int(input())))
# import random
# scorebot = 0
# scoreplayer = 0
# input2 = int(input("how many times repeated for the game? "))
# for i in range (input2):
#     rps = ("scissors", "rock", "paper",)
#     random1 = random.randrange(0,2)
#     input1 = input("you:")
#     random1 = random.randrange(0,2)
#     print(f"bot:{rps[random1]}")
#     if input1 not in rps:
#         while input1 not in rps: 
#             input1 = input("rock, paper, scissors. you:")
#             if input1 in rps:
#                 break    
#     match input1:
#         case input1 if input1 == "rock" and rps[random1] == "paper":
#             print("u lose.")
#             scorebot +=1
#         case input1 if input1 == "paper" and rps[random1] == "scissors":
#             print("u lose.")
#             scorebot +=1
#         case input1 if input1 == "scissors" and rps[random1] == "rock":
#             print("u lose.")
#             scorebot +=1
#         case input1 if input1 == rps[random1]:
#             print("it's a tie.")    
#         case _:
#             print("u win.")
#             scoreplayer +=1
# print(f"final result: player:{scoreplayer}, bot:{scorebot}")        
# def findNumberIndexInFibonacci(n):
#     if n <= 1:
#         return 1
#     return findNumberIndexInFibonacci(n-1) + findNumberIndexInFibonacci(n-2)
    
# print(findNumberIndexInFibonacci(5))

# 1,1,2,3,5,8,...
# def SUMOFinput(n):
#     temp = str(n)
#     c = len(temp)-1
#     if c <=0 :
#         return int(n)
#     return SUMOFinput(temp[:c]) + int(temp[c])
# print(SUMOFinput(12345))
# def tinhtong(n):
#     if n <= 1:
#         return 2
   
#     return 2**(tinhtong(n-1))+2**n
# print(tinhtong(10)
# import math
# counter=0
# counter1=0
# counter2=0
# co=1
# import tkinter as tk
# root = tk.Tk()
# label = tk.Label(root, text="0", font=("Times New Roman", 15))
# label1=tk.Label(root, text='''INSTRUCTIONS: Type a number, then press enter, type another number, after that, press =, then choose your operator.
# Use the reset button to reset the calculator.''', font=("Times New Roman", 15))
# label1.pack()
# label.pack()
# def a():
#     global counter
#     counter= int(str(counter)+"1")
#     label.config(text = counter)
# def b():
#     global counter
#     counter= int(str(counter)+"2")
#     label.config(text = counter)
# def c():
#     global counter
#     counter= int(str(counter)+"3")
#     label.config(text = counter)
# def d():
#     global counter
#     counter= int(str(counter)+"4")
#     label.config(text = counter)
# def e():
#     global counter
#     counter= int(str(counter)+"5")
#     label.config(text = counter)
# def f():
#     global counter
#     counter= int(str(counter)+"6")
#     label.config(text = counter)
# def g():
#     global counter
#     counter= int(str(counter)+"7")
#     label.config(text = counter)
# def h():
#     global counter
#     counter= int(str(counter)+"8")
#     label.config(text = counter)
# def i():
#     global counter
#     counter= int(str(counter)+"9")
#     label.config(text = counter)
# def j():
#     global counter
#     counter= int(str(counter)+"0")
#     label.config(text = counter)
# def k():
#     global co
#     global counter
#     global counter2
#     global counter1
#     if co==1:
#         counter1 = counter
#         counter=0
#         co+=1
#     else:
#         counter2=counter
#         counter=0
#         co+=1
# def l():
#     global counter
#     global counter1
#     counter1=int(counter1)
#     global counter2
#     counter2=int(counter2)
#     counter=counter1+counter2
#     label.config(text=counter) 
#     global co
#     counter1=counter
# def m():
#     global counter
#     global counter1
#     counter1=int(counter1)
#     global counter2
#     counter2=int(counter2)
#     counter=counter1-counter2
#     label.config(text=counter) 
#     counter1=counter
# def n():
#     global counter
#     global counter1
#     counter1=int(counter1)
#     global counter2
#     counter2=int(counter2)
#     counter=counter1*counter2
#     label.config(text=counter) 
#     counter1=counter
# def o():
#     global counter
#     global counter1
#     counter1=int(counter1)
#     global counter2
#     counter2=int(counter2)
#     counter=counter1/counter2
#     label.config(text=counter) 
#     counter1=counter
# def p():
#     global counter
#     global counter1
#     counter1=int(counter1)
#     global counter2
#     counter2=int(counter2)
#     counter=counter1**counter2
#     label.config(text=counter)
#     counter1=counter
# def q():
#     global counter
#     global counter1
#     counter=math.sqrt(counter1)
#     counter1=counter
#     label.config(text=counter)
# def r():
#     global counter
#     global co
#     co=1    
#     counter=0
    
    
    
    
                        
                               
# button1 = tk.Button(root, text="1", font=("Comic Sans MS", 10), command=a)
# button2 = tk.Button(root, text="2", font =("Comic Sans MS", 10), command=b)
# button3 = tk.Button(root, text="3", font =("Comic Sans MS", 10), command=c)
# button4 = tk.Button(root, text="4", font =("Comic Sans MS", 10), command=d)
# button5 = tk.Button(root, text="5", font =("Comic Sans MS", 10), command=e)
# button6 = tk.Button(root, text="6", font =("Comic Sans MS", 10), command=f)
# button7 = tk.Button(root, text="7", font =("Comic Sans MS", 10), command=g)
# button8 = tk.Button(root, text="8", font =("Comic Sans MS", 10), command=h)
# button9 = tk.Button(root, text="9", font =("Comic Sans MS", 10), command=i)
# button0 = tk.Button(root, text="0", font =("Comic Sans MS", 10), command=j)
# buttonplus = tk.Button(root, text="+", font=("Comic Sans MS", 10), command=l)
# buttonminus = tk.Button(root, text="-", font=("Comic Sans MS", 10), command=m)
# buttontimes = tk.Button(root, text="*", font=("Comic Sans MS", 10), command=n)
# buttondivide = tk.Button(root, text="/", font=("Comic Sans MS", 10), command=o)
# buttonpower = tk.Button(root, text="^", font=("Comic Sans MS", 10), command=p)
# buttonsqrt = tk.Button(root, text="√", font=("Comic Sans MS", 10), command=q)
# buttonreset = tk.Button(root, text="Reset", font=("Comic Sans MS", 10), command=r)
# buttonenter=tk.Button(root, text="Enter", font=("Comic Sans MS", 10), command=k)
# button1.pack()
# button2.pack()
# button3.pack()
# button4.pack()
# button5.pack()
# button6.pack()
# button7.pack()
# button8.pack()
# button9.pack()
# button0.pack() 
# buttonplus.pack() 
# buttonminus.pack()
# buttontimes.pack()
# buttondivide.pack()
# buttonpower.pack()
# buttonsqrt.pack()
# buttonenter.pack()
# buttonreset.pack()
     
# root.mainloop()
# while True:
#     label.config(text=counter) 
#     print(counter1, counter2)  

# # n, k = map(int, input().split())
# # list1 = list(map(int,input().split()))
# # count = 0
# # temp1 = list1[k-1]
# # for i in range(k):
# #     if list1[i]>=temp1 and list1[i] >0:
# #         count+=1
    
# # print(count)
# input1 = input().split("+")
# a = sorted(input1)
# a = "+".join(a)
# t = 'abc'
# list1=[]
# ta=''
# for i in range(1, len(t)+1):
#     list1.append(t[int('-'+str(i))])
#     ta="".join(list1)
# print(ta)
s=input()
print(len(s))
print(s[0], s[-1])
print(s.count("a"))
if len(s)>1:
    print("chuoi khong rong")
else:
    print("chuoi rong")
print(s.upper())
print(len(s.split()))
print(s[::-1])
if s==s[::1]:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
ac=0
for i in range(len(s)):
    if s[i].isnumeric():
        ac+=1
print(ac)
print(s.replace(" ", ""))       