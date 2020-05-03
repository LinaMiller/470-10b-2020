"""
Здравствуйте, 10б!

Предлагаю вам принять участие в создании коллективного психологического
портрета нашей группы. Для этого используем известный тест,
связанный с дорисовыванием кружочков.
)))
Перед вам заготовка программы. Нарисованы 15 окружностей. Они пронумерованы,
0..14
Ваша задача, выбрать себе кружок и написать функцию,
которая дорисует что-то на вашем кружочке.

"""

"""
Запишите сюда название функции, автора и номер вашей окружности.

0, mll, Миллер Лина Львовна
1,
2,

"""

from tkinter import *


# --- Miller Lina Lvovna ---------------------
def mll(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="#ffff77", outline="#ffaa77", width=2)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    nose = canvas.create_polygon(x-5, y+5, x, y-5, x+5, y+5, fill="#ffaa77")
    eye_right = canvas.create_oval(x-27, y-22, x-13, y-8, fill="blue", outline="blue")
    eye_left = canvas.create_oval(x+13, y-22, x+27, y-8, fill="blue", outline="blue")
    mouth = canvas.create_arc(x-20, y-5, x+20, y+35, start=190, extent=160,
                              fill="#ffaa77", outline="red", width=5, style=ARC)
    #h1 = canvas.create_arc(x+30, y-50, x+60, y-20, start=20, extent=350,
    #                          style=ARC, outline="red", width=5)

    b1 = canvas.create_polygon(x-35, y-35, x-50, y-20, x-60, y-25,
                               x-35, y-35, x-20, y-50, x-40, y-55,
                               fill="green")


# --- ??? ---------------------    

# --- ??? ---------------------

# --- ??? ---------------------





# --- main ---------------------    

root = Tk()
root.geometry("900x600+0+0")
root.title("Hello, 10b!")

canvas = Canvas(root, width=896, height=596, bg="white") 
canvas.pack()


r = 50
x = r + 40
y = r + 100
list_circles = []
for k in range(3):
    for i in range(5):
        a = canvas.create_oval(x-r, y-r, x+r, y+r, outline="black",
                               fill="white", width=5)
        x += 2 * r + 80
        list_circles.append(a)
    x = r + 40
    y += 2 * r + 60
'''
for k in range(15):
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")
'''
# --- Miller Lina Lvovna ---------------------    
mll(list_circles, 0)

# --- ??? ---------------------    

# --- ??? ---------------------

# --- ??? ---------------------



canvas.mainloop()


