import tkinter as tk


def paint(event, selected_colour):
    '''Draws a line following the user mouse cursor'''
    x1, y1 = event.x-1, event.y-1
    x2, y2 = (event.x+1), (event.y+1)
    canvas.create_line(x1, y1, x2, y2, fill=selected_colour, width=5)


def change_colour(selected_colour):
    '''Changes the colour used to draw'''
    global current_colour
    current_colour = selected_colour


def clear(canvas):
    '''Clear all drawn objects from the screen'''
    canvas.delete('all')

foreground_colour = 'white'
current_colour = 'black'

# Create the window
root = tk.Tk()
root.title("Whiteboard")
root.config(background='white')

# Create a canvas object and place it at the bottom of the window
canvas = tk.Canvas(root, borderwidth=0, highlightthickness=0, background='#e3e5e8')
canvas.grid(column=0, row=1, columnspan=5)
canvas.bind("<B1-Motion>", lambda event: paint(event, current_colour))

# Create and style buttons
red_button = tk.Button(text='red',
                       foreground='white',
                       background='red',
                       relief='flat',
                       command=lambda: change_colour('red')
                       )

blue_button = tk.Button(text='blue',
                        foreground='white',
                        background='blue',
                        relief='flat',
                        command=lambda: change_colour('blue')
                        )

green_button = tk.Button(text='green',
                         foreground='white',
                         background='green',
                         relief='flat',
                         command=lambda: change_colour('green')
                         )

black_button = tk.Button(text='black',
                         foreground='white',
                         background='black',
                         relief='flat',
                         command=lambda: change_colour('black')
                         )

clear_button = tk.Button(text='Clear',
                         fg='black',
                         bg='#c4c4c4',
                         relief='flat',
                         command=lambda: clear(canvas)
                         )
# Place buttons horizontally above drawing area
red_button.grid(column=0, row=0)
blue_button.grid(column=1, row=0)
green_button.grid(column=2, row=0)
black_button.grid(column=3, row=0)
clear_button.grid(column=4, row=0)

root.mainloop()
