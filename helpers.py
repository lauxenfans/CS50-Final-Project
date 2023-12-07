import csv
import datetime
import pytz
import requests
import subprocess
import urllib
import uuid

#sava imports
from flask import redirect, render_template, session
from functools import wraps
from tkinter.colorchooser import askcolor
import tkinter as tk
from tkinter import ttk

import time
from tkinter import filedialog, messagebox
from tkinter import filedialog, Tk, Button, Canvas
import random
from PIL import ImageGrab, Image, ImageDraw

def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

#whiteboard class
class Whiteboard:
    def __init__(self, canvas):
        self.canvas = canvas
        self.eraser_active = False
        self.brush_size = 5
        self.shade = 'black'
        self.current_color = 'black'

    # generate a random drawing
    def generate_random_drawing(self):
        colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "black"]

        # start with a blank canvas
        self.canvas.delete("all")

        # dynamically determine canvas dimensions (bc it might've been resized)
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

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
                self.canvas.create_line(x1, y1, x2, y2, fill=color, width=random.randint(1, 5))
            elif shape_type == "rectangle":
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color, width=random.randint(1, 5))
            elif shape_type == "oval":
                self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color, width=random.randint(1, 5))


    def save_canvas_as_image(self):
        try:
            self.canvas.focus_set()
            time.sleep(1)
            # Ask the user for a filename
            file_name_png = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

            # Save the canvas content and pixel grab as a PNG file
            if file_name_png:
                # Create an empty image with the same size as the canvas
                canvas_image = Image.new("RGB", (self.canvas.winfo_width(), self.canvas.winfo_height()), color="white")

                # Draw the canvas content onto the image
                x, y, width, height = self.canvas.winfo_rootx(), self.canvas.winfo_rooty(), self.canvas.winfo_width(), self.canvas.winfo_height()
                canvas_image.paste(ImageGrab.grab(bbox=(x, y, x + width, y + height)))

                # Capture pixel colors
                pixel_grab_image = ImageGrab.grab(bbox=(x, y, x + width, y + height))

                # Save the canvas image as a PNG file
                canvas_image.save(file_name_png, format="PNG")

                # Save pixel grab as a separate PNG file
                pixel_grab_image.save(f"{file_name_png.replace('.png', '_pixel_grab.png')}", format="PNG")

                # Show success message
                messagebox.showinfo("Success", f"Whiteboard and pixel grab saved as {file_name_png}")
        except Exception as e:
            # Show error message
            messagebox.showerror("Error", f"Failed to save whiteboard and pixel grab: {e}")

    # use Antialiasing to blend adjacent pixels to make lines look smoother when the mouse is moved quickly
    # according to the tkinter documentation: 
    # the value of 'splinesteps' indicates the number of control points to use for spline interpolation, which determines the smoothness of the line.

    def paint(self, event, shade):

        # if eraser is active, find which items overlap with the mouse position
        if self.eraser_active:
            x1 = event.x - 2
            y1 = event.y - 2
            x2 = event.x + 2
            y2 = event.y + 2
            erasable = self.canvas.find_overlapping(x1, y1, x2, y2)
            for things in erasable:
                self.canvas.delete(things)
        
        # if eraser mode is not active (a.k.a. I want to draw)
        else:
            #sets the color of ink to the current color.
            shade = self.current_color
            x1 = (event.x - self.brush_size)
            y1 = (event.y - self.brush_size)
            x2 = (event.x + self.brush_size)
            y2 = (event.y + self.brush_size)

            # create oval shapes (that simulate a line)
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.current_color, outline=self.current_color)

    # create a text imput 
    def draw_text(self, event):
        input_text = self.text_entry.get()

        # if there is text to input
        if input_text:
            # style the font input
            font_size_val = self.font_size.get()
            font_style = ("Helvetica", font_size_val, "bold")
            # input the text into the canvas based off the binding defined later
            self.canvas.create_text(event.x, event.y, text=input_text, fill="black", font=font_style)

    def toggle_eraser(self):
        # if it is not eraser mode, turn it into eraser mode
        # if it is eraser mode, turn it into not eraser mode 
        # these might be my favorite two lines of code here

        # global eraser_active
        self.eraser_active = not self.eraser_active

        # Display message so user knows when it is or isn't eraser mode
        message = "Eraser Active" if self.eraser_active else ""
        self.eraser_message_label.config(text=message)

    # color picker menu based off hardware and software of user
    # thank you tkinter documentation 
    def color_picker(self):
        # global shade, current_color
        color = askcolor()
        # color will give both the hex and rgb of the chosen color, so I need to undex to 
        # color[1] for my draw function to use it
        #shade = color[1]
        #self.current_color = shade
        if color[1] is not None:
            shade = color[1]
            self.current_color = shade

    def change(self, shade):
        # global current
        self.current = shade

    # clear function erases everything from canvas (thank you tkinter documentation)
    def clear(self):
        self.canvas.delete('all')

    # changes brush size based off value from slider
    def update_brush_size(self, value):
        #global brush_size
        self.brush_size = int(value)
