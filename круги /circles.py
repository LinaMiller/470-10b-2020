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
1, georgyteterin, Тетерин Георгий
2, nik, Пономарев Никита
3, eva, Пономарева Ева
4, dima, DimaLedentsov
5, andrey, Малышев Андрей
6, Lera, Topchiy Lera
7, SenyaHaha, Лукин Арсений
8, ladvishchenko, Ладвищенко Александр
9, polly, Ефимова Полина


...


"""
from tkinter import *


# --- Miller Lina Lvovna ---------------------
def mll(ls_circle, k):
    """
     Функция рисует смайлик в кружке.
     Параметры функции:
     ls_circle - список координат центров окружностей
     k - номер кружка, который я собираюсь раскрашивать.
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

# --- Dmitriy Ledentsov  ---------------------
def dima(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="grey", outline="black", width=3)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-30, y-18,x-10 , y-8, fill="pink1",outline="#e7e784")
    eye_left = canvas.create_oval(x+10, y-18, x+30, y-8, fill="pink1", outline="#e7e784")
    
    pupil_right = canvas.create_oval(x-24, y-18, x-16, y-11, fill="black",outline="black")
    pupil_left = canvas.create_oval(x+16, y-18, x+24, y-11, fill="black",outline="black")
    mouth = canvas.create_line(x-25,y+18, x+25, y+18, fill="black",width=3)


# --- Efimova Polina ---------------------
def polly(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="#f7dfd6", outline="#efc3bd", width=5)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-27, y-22,x-13 , y-8, fill="white",outline="#e7e784")
    eye_right1 = canvas.create_oval(x-24, y-15, x-16, y-8, fill="black",outline="black")
    eye_left = canvas.create_oval(x+13, y-22, x+27, y-8, fill="white", outline="#e7e784")
    eye_left1 = canvas.create_oval(x+16, y-15, x+24, y-8, fill="black",outline="black")
    rot = canvas.create_oval(x-25,y+10, x+25, y+30, fill="#f73110",outline="#f73110")
    rrot = canvas.create_oval(x-25,y+5, x+25, y+25, fill="#f7dfd6",outline="#f7dfd6")
    tongue = canvas.create_oval(x-9,y+27, x+9, y+35, fill="#f73110",outline="#f73110")
    palka = canvas.create_line(x,y+28,x,y+34,fill="black",width=1)
    
# --- Teterin Georgy ---------------------
def georgyteterin(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="lightsteelblue1", outline="lightsteelblue3", width=3)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-27, y-22,x-13 , y-8, fill="pink1",outline="#e7e784")
    eye_left = canvas.create_oval(x+13, y-22, x+27, y-8, fill="pink1", outline="#e7e784")
    pupil_right = canvas.create_oval(x-24, y-18, x-16, y-11, fill="black",outline="black")
    pupil_left = canvas.create_oval(x+16, y-18, x+24, y-11, fill="black",outline="black")
    mouth = canvas.create_line(x-25,y+18, x+25, y+25, fill="black",width=3)


# --- Ponomarev Nikita ---------------------
def nik (ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="yellow", outline="black", width=2)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-27, y-22, x-13, y-8, fill="blue", outline="blue")
    eye_left = canvas.create_oval(x+13, y-22, x+27, y-8, fill="blue", outline="blue")
    mouth = canvas.create_arc(x-40, y-5, x+40, y+25, start=190, extent=160,
                              fill="black", outline="black", width=5, style=ARC)
    glass_left =canvas.create_oval(x+10, y-25, x+ 30, y-5,outline="black")
    glass_right = canvas.create_oval(x-30, y-25, x-10, y-5, outline="black")
    glass = canvas.create_line(400,135,500,135, fill="black")

# --- Ponomareva Eva ---------------------
def eva(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="indian red", outline="navajo white", width=4)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-27, y-22, x-13, y-8, fill="lavender", outline="white",width=2)
    eye_left = canvas.create_oval(x+13, y-22, x+27, y-8, fill="lavender", outline="white",width=2)
    eye_right1 = canvas.create_oval(x-24, y-18, x-16, y-11, fill="black",outline="black",width=0.5)
    eye_left1 = canvas.create_oval(x+16, y-18, x+24, y-11, fill="black",outline="black",width=0.5)
    mouth = canvas.create_arc(x-20, y-5, x+20, y+15, start=190, extent=160,
                              fill="red", outline="lemon chiffon", width=4, style=ARC)
    mouth1 = canvas.create_arc(x-22, y-5, x+22, y+35, start=160, extent=220,
                              fill="red", outline="lemon chiffon", width=4, style=ARC)

# --- Andrey Malichev ---------------------
def andrey(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="green", outline="green", width=3)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    
    pupil_right = canvas.create_oval(x-24, y-18, x-16, y-11, fill="black",outline="black")
    pupil_left = canvas.create_oval(x+16, y-18, x+24, y-11, fill="black",outline="black")
    mouth = canvas.create_arc(x-20, y-9, x+20, y+25, start=190, extent=160,
                              fill="red", outline="red", width=4, style=ARC)


# --- Lukin Arseny ---------------------

def SenyaHaha(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="yellow2", outline="gold", width=5)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-27, y-22,x-13 , y-6, fill="lightcyan2",outline="#e7e784")
    eye_left = canvas.create_oval(x+13, y-22, x+27, y-6, fill="lightcyan2", outline="#e7e784")
    in_eye_right = canvas.create_oval(x-24, y-18, x-16, y-8, fill="black",outline="black")
    in_eye_left = canvas.create_oval(x+16, y-18, x+24, y-8, fill="black",outline="black")
    smile = canvas.create_oval(x-25,y+15, x+25, y+35, fill="indianred2",outline="#f73110")
    lip = canvas.create_oval(x-25,y+5, x+25, y+25, fill="yellow2",outline="#f7dfd6")


# --- Valeria Topchiy ---------------------
def Lera(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="yellow", outline="black", width=2)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-27, y-22, x-13, y-8, fill="pink", outline="white",width=2)
    eye_left = canvas.create_oval(x+13, y-22, x+27, y-8, fill="pink", outline="white",width=2)
    eye_right1 = canvas.create_oval(x-24, y-18, x-16, y-11, fill="black",outline="black",width=0.5)
    eye_left1 = canvas.create_oval(x+16, y-18, x+24, y-11, fill="black",outline="black",width=0.5)
    mouth = canvas.create_arc(x-20, y-9, x+20, y+25, start=190, extent=160,
                              fill="red", outline="red", width=4, style=ARC)
   

# --- Ladvishchenko Alexandr  ---------------------
def ladvishchenko(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="black", outline="white", width=3)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-26, y-23,x-14 , y-8, fill="red",outline="#e7e784")
    eye_left = canvas.create_oval(x+10, y-18, x+30, y-8, fill="red", outline="#e7e784")
    
    pupil_right = canvas.create_oval(x-24, y-18, x-16, y-11, fill="black",outline="black")
    pupil_left = canvas.create_oval(x+16, y-18, x+24, y-11, fill="black",outline="black")
    mouth = canvas.create_line(x-10,y+18, x+10, y+18, fill="red",width=3)

# --- Birukova Ulyana ----------------------------
def Ulyana(Is_circle, k):
    """
     mill -
    """
    face = Is_circle[k]
    canvas.itemconfig(face, fill="pink", outline="pink", width=2)
    n =(k//5)
    m  = (k  %  5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-27,y-22,x-13,y-8,fill="white",outline="pink",width=2)
    eye_left = canvas.create_oval(x+13,y-22,x+27,y-8,fill="white",outline="pink",width=2)
    pupil_right = canvas.create_oval(x-24,y-18,x-16,y-11,fill="black",outline="black",width=0.5)
    pupil_left = canvas.create_oval(x+16,y-18,x+24,y-11,fill="black",outline="black",width=0.5)
    mouth=canvas.create_arc(x-15,y-9,x+15,y+25,start=190,extent=160,fill="red",width=4)
    hat_brim = canvas.create_line(x-70,y-40,x+70,y-40,fill="brown",width=3)
    hat=canvas.create_rectangle(x+30,y-40,x-30,y-60,outline="brown",fill="brown",width=2)
    flower = canvas.create_polygon(x-35, y-40, x-50, y-20, x-60, y-25,
                               x-35, y-40, x-20, y-50, x-40, y-55,
                               fill="purple")

    
# ---  ----------------------------
root = Tk()
root.geometry("900x600+20+20")
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

# --- Dmytry Ledentsov ---------------------
dima(list_circles, 4)
     
# --- Efimova Polina ---------------------
polly(list_circles, 9)

# --- Teterin Georgy ---------------------
georgyteterin(list_circles, 1)

# --- Ponomarev Nikita ---------------------
nik(list_circles, 2)

# --- Ponomareva Eva ---------------------
eva(list_circles, 3)


# --- Lukin Arseny ---------------------
SenyaHaha(list_circles, 7)

# --- Malichev Andrey ---------------------
andrey(list_circles, 5)
# --- Topchiy Lera ---------------------
Lera(list_circles, 6)

# --- Ladvishchenko Alexandr ---------------------
ladvishchenko(list_circles, 8)

# --- Birukova Ulyana ---------------------
Ulyana(list_circles, 10)


canvas.mainloop()





