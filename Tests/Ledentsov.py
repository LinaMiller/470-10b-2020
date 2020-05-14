from tkinter import *

x = 10
y = 10
a = 50
b = 50

x_vel = 5
y_vel = 4

def move():

    global x
    global y
    global x_vel
    global y_vel
    if x < 0:
        x_vel = 5
    if x > 500:
        x_vel = -5
    if y < 0:
        y_vel = 5
    if y > 500:
        y_vel = -5
    canvas1.move(circle, x_vel, y_vel)
    coordinates = canvas1.coords(circle)
    x = coordinates[0]
    y = coordinates[1]
    window.after(33, move)

window   = Tk()
window.geometry("500x500")

canvas1=Canvas(window, height = 500, width= 500)
canvas1.grid (row=0, column=0, sticky=W)
coord = [x, y, a, b ]

circle = canvas1.create_oval(coord, outline="red", fill="red")


coord = [0,0,500,500]
rect2 = canvas1.create_rectangle(coord, outline="Blue")

move()

window.mainloop ()
