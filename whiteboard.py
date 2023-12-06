from tkinter.colorchooser import askcolor
import tkinter as tk
from tkinter import ttk

# use Antialiasing to blend adjacent pixels to make lines look smoother when the mouse is moved quickly
# according to the tkinter documentation: 
# the value of 'splinesteps' indicates the number of control points to use for spline interpolation, which determines the smoothness of the line.
def paint(event, shade):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_line(x1, y1, x2, y2, width=5, fill=shade, splinesteps = 256)

def color_picker():
   color = askcolor()
   global shade 
   shade = color[1]
   #return(color[1])

def change(shade):
    global current
    current = shade

def clear(canvas):
    '''Clear all drawn objects from the screen'''
    canvas.delete('all')


# make and style the window
root = tk.Tk()
root.title('WriteRight - Canvas')
root.resizable(True, True)

# make a frame that holds the canvas (and sizegrip!)
frame = tk.Frame(root)
frame.pack(fill='both', side=tk.BOTTOM, expand=True)

# make the canvas
canvas = tk.Canvas(frame, bg='white')
canvas.pack(fill='both', expand=True)

# make the sizegrip element
sizegrip = ttk.Sizegrip(frame)
sizegrip.pack(side='bottom', anchor='se')
#root.geometry("500x500")

root.config(background='black')

shade = 'black'
current_color = 'black'
# define what happens when user clicks and drags the left mouse button <B1-Motion>
# lambda is a keyword for a "throwaway" function that python uses to access a small "anonymous" function
canvas.bind("<B1-Motion>", lambda event: paint(event, shade))

custom = tk.Button(root, text ="Custom Color", command = color_picker)
custom.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)

clear_b = tk.Button(text='Clear', fg='black', bg='#c4c4c4', relief='flat', command=lambda: clear(canvas))
clear_b.pack(side=tk.RIGHT, fill=tk.BOTH, padx=5, pady=5)



root.mainloop()