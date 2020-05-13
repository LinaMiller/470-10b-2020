from tkinter import *
import time
class Ball(object):
    def __init__(self,c,color):
        self.c=c
        self.ball2=c.create_oval(10,10,25,25,fill=color)
        self.x=100
        self.y=100
        self.vx=1
        self.vy=1
    def draw(self):
        self.c.move(self.ball2,self.vx,self.vy)
        self.x+=self.vx
        self.y+=self.y
def motion():
    c.move(ball, x_ball_speed, y_ball_speed)    
    if x_ball_speed > 0:
        if (c.coords(ball)[0] + c.coords(ball)[2])/2 < x:
            root.after(30, motion)
    elif x_ball_speed < 0:
        if (c.coords(ball)[0] + c.coords(ball)[2])/2 > x:
            root.after(30, motion)
 
def click_move(event):
    global x, y, x_ball_speed, y_ball_speed
    x = event.x
    y = event.y
    x_ball_speed = (x - (c.coords(ball)[0] + c.coords(ball)[2])/2) / 100
    y_ball_speed = (y - (c.coords(ball)[1] + c.coords(ball)[3])/2) / 100
 
    motion()
 
    return x, y, x_ball_speed, y_ball_speed
 
 
root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140, fill='green', outline='green')
x = 300
y = 200
x_ball_speed = 1
y_ball_speed = 0
b=Ball(c,'red')
b.draw()

 
c.bind('<Button-1>', click_move)
motion()

root.mainloop()
