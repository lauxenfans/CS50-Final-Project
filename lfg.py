from tkinter.colorchooser import askcolor
import tkinter as tk
from tkinter import ttk
import time
from tkinter import filedialog, messagebox
from tkinter import filedialog, Tk, Button, Canvas
import random
from PIL import ImageGrab, Image, ImageDraw
import pygetwindow as gw
import tkcap
import os

# some things that'll be helpful
brush_size = 5
eraser_active = False
shade = 'black'
current_color = 'black'

class Whiteboard:
    # generate a random drawing
    def generate_random_drawing(canvas):
        colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "black"]

        # start with a blank canvas
        canvas.delete("all")

        # dynamically determine canvas dimensions (bc it might've been resized)
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        # generate a random number of shapes
        for x in range(random.randint(15, 20)):
            
            #determine shape type and color "randomly", using calls from the documentation
            shape_type = random.choice(["line", "rectangle", "oval"])
            color = random.choice(colors)

            # to make the shapes appear more random, randomly set their coordinates based off canvas dimensions
            x1 = random.randint(0, canvas_width)
            y1 = random.randint(0, canvas_height)
            x2 = random.randint(0, canvas_width)
            y2 = random.randint(0, canvas_height)

            # actually generate the shapes based off all the previous "random" criteria
            if shape_type == "line":
                canvas.create_line(x1, y1, x2, y2, fill=color, width=random.randint(1, 5))
            elif shape_type == "rectangle":
                canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color, width=random.randint(1, 5))
            elif shape_type == "oval":
                canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color, width=random.randint(1, 5))


    def save_canvas_as_image():
        screenshot_path = "/Users/savat1/Mirror/Mirror/GitHub/CS50-Final-Project/screenshot.jpg"

        try:
            cap = tkcap.CAP(root)
            cap.capture(screenshot_path)
            print("Screenshot saved at:", screenshot_path)
        except Exception as e:
            print("Error capturing screenshot:", e)

        try:
            # Optionally, add more details about the error, if any
            with open(screenshot_path, 'wb') as f:
                pass
        except Exception as e:
            print("Error saving file:", e)


    

   
    # use Antialiasing to blend adjacent pixels to make lines look smoother when the mouse is moved quickly
    # according to the tkinter documentation: 
    # the value of 'splinesteps' indicates the number of control points to use for spline interpolation, which determines the smoothness of the line.

    def paint(event, shade):
        # define global variables that impact painting (or the opposite: erasing)
        global eraser_active, current_color

        # if eraser is active, find which items overlap with the mouse position
        if eraser_active:
            x1 = event.x - 2
            y1 = event.y - 2
            x2 = event.x + 2
            y2 = event.y + 2
            erasable = canvas.find_overlapping(x1, y1, x2, y2)
            for things in erasable:
                canvas.delete(things)
        
        # if eraser mode is not active (a.k.a. I want to draw)
        else:
            #determine color of ink, can be adjusted later
            current_color = shade
            x1 = (event.x - brush_size)
            y1 = (event.y - brush_size)
            x2 = (event.x + brush_size)
            y2 = (event.y + brush_size)

            # create oval shapes (that simulate a line)
            canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)

    # create a text imput 
    def draw_text(event):
        input_text = text_entry.get()

        # if there is text to input
        if input_text:
            # style the font input
            font_size_val = font_size.get()
            font_style = ("Helvetica", font_size_val, "bold")
            # input the text into the canvas based off the binding defined later
            canvas.create_text(event.x, event.y, text=input_text, fill="black", font=font_style)

    def toggle_eraser():
        # if it is not eraser mode, turn it into eraser mode
        # if it is eraser mode, turn it into not eraser mode 
        # these might be my favorite two lines of code here

        global eraser_active
        eraser_active = not eraser_active

        # Display message so user knows when it is or isn't eraser mode
        message = "Eraser Active" if eraser_active else ""
        eraser_message_label.config(text=message)

    # color picker menu based off hardware and software of user
    # thank you tkinter documentation 
    def color_picker():
        global shade, current_color
        color = askcolor()
        # color will give both the hex and rgb of the chosen color, so I need to undex to 
        # color[1] for my draw function to use it
        shade = color[1]
        current_color = shade

    def change(shade):
        global current
        current = shade

    # clear function erases everything from canvas (thank you tkinter documentation)
    def clear(canvas):
        canvas.delete('all')

    # changes brush size based off value from slider
    def update_brush_size(value):
        global brush_size
        brush_size = int(value)

# make and the window, and make it resizable on both axes
root = tk.Tk()
root.title('WriteRight - Canvas')
root.resizable(True, True)
root.config(background='black')

# make a frame that holds the canvas (and sizegrip!)
frame = tk.Frame(root)
frame.pack(fill='both', side=tk.BOTTOM, expand=True)

# make the canvas widget
canvas = tk.Canvas(frame, bg='white')
canvas.pack(fill='both', expand=True)

# define what happens when user clicks and drags the left mouse button <B1-Motion>
# lambda is a keyword for a "throwaway" function that python uses to access a small "anonymous" function
# got help in office hours for how to use lambda (and also when its no necessary)
canvas.bind("<B1-Motion>", lambda event: Whiteboard.paint(event, shade))
canvas.bind("<Double-Button-1>", lambda event: Whiteboard.draw_text(event))

# make the sizegrip element
sizegrip = ttk.Sizegrip(frame)
sizegrip.pack(side='bottom', anchor='se')

# make some buttons!

#custom color button
custom_b = tk.Button(root, text="Color", command=Whiteboard.color_picker)
custom_b.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

# eraser button
eraser_button = tk.Button(root, text="Eraser", command=Whiteboard.toggle_eraser)
eraser_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

# a label that shows the brush scale slider
brush_label = tk.Label(root, text="Brush Size:")
brush_label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

# the actual brush size adjuster
brush_size_b = tk.Scale(root, from_=1, to=30, orient=tk.HORIZONTAL, length=100, command=Whiteboard.update_brush_size)
brush_size_b.set(brush_size)
brush_size_b.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

# text entry 
text_entry = tk.Entry(root, width=30)
text_entry.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

# font size variable to be adjusted (default 12)
font_size = tk.IntVar()
font_size.set(12)

# font size slider
font_size_slider = tk.Scale(root, from_=8, to=100, orient=tk.HORIZONTAL, variable=font_size)
font_size_slider.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

# random drawing button
random_drawing_b = tk.Button(root, text="Random", command=lambda: Whiteboard.generate_random_drawing(canvas))
random_drawing_b.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

# clear button
clear_b = tk.Button(root, text='Clear', command=lambda: Whiteboard.clear(canvas))
clear_b.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

# save button
save_button = tk.Button(root, text="Save", command=Whiteboard.save_canvas_as_image)
save_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)


# Create a label to display the eraser message
eraser_message_label = tk.Label(root, text="", fg="red")
eraser_message_label.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()