from tkinter import *
root=Tk()
canv=Canvas(root,width=500,height=500,bg="lightblue")
def change():
    if var.get() == 0:
        canv.itemconfig(poly,fill="red")
    elif var.get() == 1:
        canv.itemconfig(poly,fill="green")
    elif var.get() == 2:
        canv.itemconfig(poly,fill="blue")
var = IntVar()
var.set(0)
red = Radiobutton(text="Красный", variable=var, value=0)
green = Radiobutton(text="Зеленый", variable=var, value=1)
blue = Radiobutton(text="Синий", variable=var, value=2)
button = Button(text="Раскрась треугольник", command=change)
poly = canv.create_polygon([90,270],[230,150],[370,270],fill="white",outline="black")
red.pack()
green.pack()
blue.pack()
button.pack()
canv.pack() 
root.mainloop()
