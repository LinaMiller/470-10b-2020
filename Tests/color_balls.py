from tkinter import *
from random import *

size = 500

window = Tk()
canvas = Canvas( window, width=size, height=size )
canvas.pack()

while True:
    col = choice( ['pink', 'red', 'orange', 'purple', 'yellow'] )
    d = randint( 0, size/5 )
    x0 = randint( 0, size - d )
    y0 = randint( 0, size - d )
    
 
    canvas.create_oval( x0, y0, x0 + d, y0 + d, fill=col )
    window.update()

    


