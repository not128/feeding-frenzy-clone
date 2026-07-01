# #phan 2: trung binh
# #6: if else so chan hay le
# num=10
# if num%2==1:
#     print("le")
# else:
#     print("chan")

# #7 while for print number from 1 to 5
# num1=1
# while num1!=6:
#     print(num1)
#     num1+=1
# #8 for i in range 0,6 print hello
# for i in range(0,6):
#     print("Hello")
# #9 check if >0 or <=0
# num2 = int(input("nhap so"))
# if num2>0:
#     print("Duong")
# else:
#     print("am hoac bang 0")
# #10 timetable 5
# for i in range(1, 11):
#     print(f"5x{i}={5*i}")
# #11 tinhtong 1 den n
# n=int(input())
# i=n-1
# while i!=0:
#     n+=i
#     i-=1
# print(n)
# #12 nguyento
# bool=False
# for i in range(2, 6):
#     if 7%i !=0 :
#         bool = True
        
# if bool:
#     print("nguyen to")
# #phan 3 kho
# #13 tong a va b
# def tinh_tong(a,b):
#     print(a+b)
# tinh_tong(3, 4)
# #14 check even
# def kiem_tra_chan(num):
#     if num%2==1:
#         return False
#     else:
#         return True
# print(kiem_tra_chan(4))
# #15 phan tu 2 of list
# numbers = [1, 2, 3, 4, 5]
# print(numbers[1])

# #16 thao tac list
# fruits = ["táo", "chuối", "cam"]
# fruits.append("dua")
# print(fruits)
# #17 max and sum
# scores = [80, 90, 70, 85]


# print(f"diem cao nhat:{max(scores)}, tong:{sum(scores)}")
# #18
# list1=[]

# for i in range(5):
#     x=int(input())
#     list1.append(x)
#     neg_inf= list1[0]
# for i in range(0, len(list1)):
#     if list1[i]>neg_inf:
#         neg_inf=list1[i]
# print(neg_inf)
# #20
# def dem_chu_so(n):
#     a=0
#     while a!=len(str(n)):
#         a+=1
#     return a
# print(dem_chu_so(4567))
# niums = [5,3,8,1]       
# for i in range(0,len(niums)-1):
#     for j in range (i+1, len(niums)):
#         if niums[i] > niums[j]:
#             niums[i], niums[j] = niums[j], niums[i]
# print(niums)           
# expand.py
# Expand 100 Hz samples to 8 kHz PCM array and save to audioClip.h

# samples = [
#     94,94,99,84,111,110,107,106,104,103,102,102,102,103,107,37,83,87,84,81,
#     104,108,106,103,101,100,99,100,100,102,21,62,63,66,47,144,137,130,126,122,
#     118,116,114,113,119,45,79,78,77,51,107,104,102,100,99,98,98,98,98,99,100,
#     101,18,61,69,46,89,89,88,89,89,90,91,92,94,92,101,106,106,107,108,103,96,
#     104,102,101,101,101,101,101,102,103,195,88,90,90,95,97,90,119
# ]

# expand_factor = 80
# expanded = []
# for val in samples:
#     expanded.extend([val] * expand_factor)

# with open("audioClip.h", "w") as f:
#     f.write("#include <PCM.h>\n")
#     f.write("#include <avr/pgmspace.h>\n\n")
#     f.write("const unsigned char audioClip[] PROGMEM = {\n")
#     for i, val in enumerate(expanded):
#         comma = "," if i < len(expanded)-1 else ""
#         f.write(f"  {val}{comma}\n")
#     f.write("};\n")

# print("Expanded array saved to audioClip.h")
# import serial

# arduino = serial.Serial('COM4', 230400)  # Replace COM3 with your port
# with open("output.pcm", "wb") as f:    # Raw PCM file
#     while True:
#         data = arduino.read(1)         # Read 1 byte
#         f.write(data)                  # Save directly
# import random as r
# import sys
# score=0
# WIDTH = 800
# HEIGHT = 800
# media = Actor("mario")
# obstacles = []
# def addobst():
#     global obst
#     global obstacles
#     obst = Actor("goomba", (WIDTH,HEIGHT-128))
    
#     obstacles.append(obst)
 
# on_ground = False
# def land():
#     global on_ground
#     media.y+=0.1
#     on_ground = True
# def useless():
#     pass


# def update():    
#     global media,score,on_ground
       
#     if keyboard.down:
#         media.y+=5
#     if keyboard.right:
#         media.x+=5
#     if keyboard.left:
#         media.x-=5 
#     media.y+=3
#     if media.y>HEIGHT-128:
#         media.y=HEIGHT-128
#         on_ground=True
        
    
#     for obst in obstacles[:]:
#         print (obst.y, media.y)
#         obst.x -=10
#         if obst.right < 0:
#             obstacles.remove(obst)
#         if obst.colliderect(media):
#             if media.y<obst.y:
#                 obstacles.remove(obst)
#                 score+=10
                
                
#             else:
#                 exit()

# def on_key_down(key):
#     global on_ground
#     if key==keys.UP and on_ground:
#         media.y-=250
#         clock.schedule_unique(land, 2)
#         on_ground = False  
    
# def draw():
#     screen.clear()
#     screen.fill((135, 206, 235))
#     global media
#     media.draw()
#     for obst in obstacles: 
#         obst.draw()

# clock.schedule_interval(addobst, r.uniform(3.0,10))
# import time
# import sys
# import random as r
# time.sleep(5)
# WIDTH = 600
# HEIGHT = 900
# downy = 2
# score=0
# pipe = Actor("pipe", (300, 800))
# pipedown = Actor("pipedown", (300, 0))
# flappybird = Actor("abc",(300, 450))
# listup = ["pipe", "pipeuplong"]
# listdown = ["pipedown", "pipedownshort"]
# def placehold():
#     pass

# def randomize():
#     global listup
#     global listdown
#     global pipe
#     global pipedown

#     pipe = Actor(r.choice(listup),(pipe.x, pipe.y))
#     pipedown = Actor(r.choice(listdown),(pipedown.x, pipedown.y))
    
# def draw():
#     global score
#     screen.clear()
#     screen.fill((135, 206, 235))
#     flappybird.draw()
#     pipe.draw()
#     pipedown.draw()
#     screen.draw.text(str(score), (300, 0), fontsize=200, color="black")
    
# def update():
#     global downy
#     global score
#     if keyboard.up:
#         flappybird.image = "abc"
#         clock.schedule_unique(placehold, 0.5)    
#         flappybird.image = "abcu"
#         downy=-4   
#     else:
#         flappybird.image = "abc"
#         downy=4
#     flappybird.y+=downy
#     pipe.x-=5
#     pipedown.x-=5
#     if pipedown.x<0 and pipe.x<0:
#         pipedown.x=800
#         pipe.x=800
#         randomize()
#         score+=1

#     if flappybird.colliderect(pipe) or flappybird.colliderect(pipedown):
#         sys.exit()
from pgzhelper import *
import random as r
WIDTH = 800
HEIGHT = 600
game_over = False
tempcount = 0
angles = [True, False]
life = 3
fishs =["fish2", "fish3", "fish4"]
fih = Actor("fish", (400, 300))
fih.scale = 0.25
fih.speed = 0
fih2 = Actor(r.choice(fishs), (300,400))
fih2.scale = 0.25
fih2.speed = 5

score=0
b=7
fihs = []
def placehold():
    pass
def difficulty():
    global b
    b-=0.25
    
def addfih():
    global fih2
    global fihs
    fih2 = Actor(r.choice(fishs), (r.uniform(0,800), r.uniform(0,600)))
    fih2.scale = r.uniform(0.07, 0.65)    
    fihs.append(fih2)
    fih2.life = 550
    fih2.speed = r.uniform(3,5)
    fih2.flip_x = r.choice(angles)
def addspecial():
    global fih2
    global fihs
    fih2 = Actor("specialfish", (r.uniform(0,800), r.uniform(0,600)))
    fih2.scale = 0.1    
    fihs.append(fih2)
    fih2.life = 300
    fih2.speed = 25
    fih2.flip_x = r.choice(angles)

def draw():
    global life
    if not game_over:
        screen.clear()
        screen.fill((0,0,139))
        fih.draw()
       
        screen.draw.text(str(score),(0,0),color="orange", fontsize = 200)
        screen.draw.text(f"HP: {life}",(280,0),color="red", fontsize=150)
        for fih2 in fihs:
            fih2.draw()
    else:
        screen.clear()
        screen.fill((0,0,139))
        screen.draw.text("GAME OVER",(25,200),color="red", fontsize=180)
        return

        
def update():
    global game_over
    global tempcount
    global score
    global life,b
    if life==0:
        game_over=True
    for fih2 in fihs:
        fih2.life-=1    
        if fih2.flip_x:
            fih2.x+=fih2.speed
        else:
            fih2.x-=fih2.speed
        if fih2.x<0:
            fih2.flip_x=True
        if fih2.x>800:
            fih2.flip_x=False           
        if fih2.life<0:
            fihs.remove(fih2)
        if fih2.colliderect(fih):
            if fih2.scale>fih.scale:
                fih.x, fih.y = r.uniform(0,800), r.uniform(0,600)
                tempcount=0
                life-=1
                b=7
                fih.scale=0.25
                score=0
                
                 
            else:
                if not fih2.image=="specialfish":
                    fihs.remove(fih2)
                    tempcount+=1
                    score+=1
                else:
                    fihs.remove(fih2)
                    tempcount+=3
                    score+=3
                    life+=1
    if game_over:
        music.stop()
        return
    else:
        if not music.is_playing('theme'): 
            music.play('theme')
    
    if keyboard.left:
        fih.speed+=0.5
        fih.x-=fih.speed
        fih.flip_x = False
        if fih.speed>10:
            fih.speed=10
    elif keyboard.right:
        fih.speed+=0.5
        fih.x+=fih.speed
        fih.flip_x= True
        if fih.speed>10:
            fih.speed=10 
    elif keyboard.up: 
        fih.speed+=0.5
        fih.y-=fih.speed
        
        if fih.speed>10:
            fih.speed=10 
    elif keyboard.down:
        fih.speed+=0.5
        fih.y+=fih.speed
        
        if fih.speed>10:
            fih.speed=10             
    else:
        fih.speed=0
    if tempcount>=3:
            tempcount=0
            fih.scale+=0.05                   
    if fih.x<=0:
            fih.x=0
    if fih.x>=800:
            fih.x = 800
    if fih.y<=0:
            fih.y=0
    if fih.y>=600:
            fih.y=600  
        
    if not music.is_playing('theme'): 
        music.play('theme')                                     
clock.schedule_interval(addfih, r.uniform(1.5,b))
clock.schedule_interval(addspecial, r.uniform(30,45))            
clock.schedule_interval(difficulty, r.uniform(30,40))
# from pgzhelper import *
# import sys
# WIDTH = 900
# HEIGHT = 700
# abc = Actor("player", (300,300))
# ghost = Actor("player2",(0,0))
# abc.scale=0.25
# ghost.x = 10000
# ghosts = []
# def addghost():
#     global ghosts
#     ghost = Actor("player2", (25,70))
#     ghost.scale=0.2
#     ghosts.append(ghost)
#     ghost.i=0
#     ghost.c=0
# def draw():
#     screen.clear()
#     screen.fill((100,200,45))
#     abc.draw()
#     for ghost in ghosts:
#         ghost.draw()
    

# def update():
#     if abc.y>=HEIGHT:
#         abc.y=HEIGHT
#     if abc.y<=0:
#         abc.y=0
#     if abc.x<=0:
#         abc.x=0
#     if abc.x>=WIDTH:
#         abc.x=WIDTH
#     for ghost in ghosts[:]:   
#         ghost.c+=1
#         if ghost.c>=250:
#             ghost.i+=1
#             if ghost.distance_to(abc)<=400:
#                 ghost.image = "ghost"
#                 ghost.scale=0.2    
#                 ghost.move_towards(abc,3.5)
#                 if ghost.i>=300:
#                         ghosts.remove(ghost)
#                         ghost.c=0
#                 if ghost.colliderect(abc):
#                     exit()
#             if not ghost.distance_to(abc) <= 400:
#                 ghost.c=0              
#     if keyboard.left:
#         abc.x-=5
#     elif keyboard.right:
#         abc.x+=5
#     elif keyboard.up:
#         abc.y-=5
#     elif keyboard.down:
#         abc.y+=5
# clock.schedule_interval(addghost,3) 
# from pgzhelper import *
# import sys, random, math
# WIDTH= 900
# HEIGHT=600
# obsts = []
# co = (45,-45)
# player = Actor("player", (300,300))
# player.scale=0.2
# def add():
#     global obsts
#     obst=Actor("abc", (100,400))
#     obsts.append(obst)
#     obst.i = 600
#     obst.angle = -45
# def draw():
#     screen.clear()
#     screen.fill((0,230,0))
#     global obsts
#     for obst in obsts:
#         obst.draw()
#     player.draw()
    
# def update():
#     if keyboard.left:
#         player.x-=5
#     elif keyboard.right:
#         player.x+=5
#     elif keyboard.down:
#         player.y+=5
#     elif keyboard.up:
#         player.y-=5

#     global obsts
#     for obst in obsts:
#         obst.i-=1
#         obst.move_forward(7)
#         if obst.i==0:
#             obsts.remove(obst)
#         if obst.colliderect(player):
#             sys.exit()
# def change_angle():
#     global obsts
#     for obst in obsts:
#         obst.angle = random.choice(co)
# clock.schedule_interval(add, 2)
# clock.schedule_interval(change_angle,0.5)