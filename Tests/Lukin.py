from tkinter import*
root=Tk()
def circle_go (event):
    key=event.keysym
    if key=="Left":
        canv.move(oval, -3,0)
        canv.move(smile, -3,0)
        canv.move(eye_1, -3,0)
        canv.move(eye_2, -3,0)
    if key=="Right":
        canv.move(oval, 3,0)
        canv.move(smile, 3,0)
        canv.move(eye_1, 3,0)
        canv.move(eye_2, 3,0)
    if key=="Up":
        canv.move(oval, 0,-3)
        canv.move(smile, 0,-3)
        canv.move(eye_1, 0,-3)
        canv.move(eye_2, 0,-3)
    if key=="Down":
        canv.move(oval, 0,3)
        canv.move(smile, 0,3)
        canv.move(eye_1, 0,3)
        canv.move(eye_2, 0,3)
canv=Canvas(root,width=700,height=1500,bg="black")
oval=canv.create_oval(5,200,500,900,fill="blue",outline="blue")
canv.bind_all("<Key>", circle_go)
smile=canv.create_arc([330,330], [380,380],start=180,extent=180,style=ARC,outline="white",width=4)
eye_1=canv.create_oval(280,230,270,220,fill="white",outline="white")
eye_2=canv.create_oval(230,230,220,220,fill="white",outline="white")


canv.pack()

root.mainloop()
