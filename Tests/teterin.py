from tkinter import*
import time
tk=Tk()
winw = 600
winh = 600
class Ball:
    def __init__ (self,canvas,r,color):
        self.canvas=canvas
        self.r=r
        

        self.vx = 1
        self.vy = 1
        self.x=245
        self.y=100
        self.id=canvas.create_oval(self.x,self.y,self.x+self.r,self.y+self.r,fill=color)
       
        self.canvas.config(width=winw, height=winh)
        self.canvas_height=winh
        self.canvas_width=winw
    def draw(self):
        self.canvas.move(self.id,self.vx,self.vy)
        
        if self.y<0+self.r:
            self.vy*=-1
        if self.y>=self.canvas_height-self.r:
            self.vy*=-1
        if self.x<0+self.r:
            self.vx*=-1
        if self.x>=self.canvas_width-self.r:
            self.vx*=-1
        self.x+=self.vx
        self.y+=self.vy
canvas=Canvas(tk,width=500,height=400)
b=Ball(canvas,10,'black')
x=1
canvas.pack()
while x==1:
    b.draw()

    tk.update()
    time.sleep(0.01)
