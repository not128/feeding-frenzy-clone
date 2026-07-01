

# for x in range(101):        # gà trống
#     for y in range(101):    # gà mái
#         z = 100 - x - y     # gà con
        
#         if z >= 0:
#             if 5*x + 3*y + 0.5*z == 100:
#                       print(x,y,z)
# import turtle

# t = turtle.Turtle()
# t.speed(3)

# t.fillcolor("orange")
# t.goto((0,0))
# t.begin_fill()

# for i in range(5):
    
#     t.forward(190) ## 6100 cạnh
#     t.right(144)
# t.penup()
# t.goto((-5,-30))    
# t.end_fill()   
# t.setheading(-90)

# t.penup()

# t.pendown()
# t.circle(100)

# turtle.done()


# d = 1
# ob=0
# list=[]
# for o in range(50):
#     list.append(d)
#     if d%5==0:
#         ob+=1
#     d+=2
# print(ob)
import  random
from pgzhelper import *
import sys
car = Actor("car", (1000,1000))
cars = [car]
abc = Actor("player", (300,300))
abc.scale = 0.3
coord=[100,200,300,400,500,600]
WIDTH = 800
coin = Actor("trans", (10000 ,10000))
coins = [coin]
score=0
HEIGHT = 600
def addcar():
    global cars
    
    car = Actor("car", (100,random.choice(coord)))
    car.scale = 0.7
    cars.append(car)
def addcoin():
    global coins
    for _ in range(random.randint(6,9)):
        coin = Actor("coin",(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)))
        coin.scale = 0.1
        coins.append(coin)

addcoin()    
def draw():
   
    global cars, coins, score
    screen.clear()
    screen.fill((100,100,100))
    for car in cars:
        car.draw()
    abc.draw()
    for coin in coins:
        coin.draw()
def update():
    global cars, coins, score
    if abc.y >= HEIGHT-50:
        print("u won, score:", score)
        sys.exit()
    
    for car in cars:
        car.x+=10 
        if car.colliderect(abc):
            print("u lose, score:", score)
            sys.exit() 
    for coin in coins:
        if coin.colliderect(abc):
            coins.remove(coin)
            score+=1
    if keyboard.left:
        abc.x-=5
    elif keyboard.right:
        abc.x+=5
    elif keyboard.up:
        abc.y-=5
    elif keyboard.down:
        abc.y+=5
    if abc.y>=HEIGHT:
        abc.y=HEIGHT
    if abc.y<=0:
        abc.y=0
    if abc.x<=0:
        abc.x=0
    if abc.x>=WIDTH:
        abc.x=WIDTH
clock.schedule_interval(addcar, 2)
