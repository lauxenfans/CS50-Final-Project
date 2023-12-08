from tkinter.colorchooser import askcolor
import tkinter as tk
from tkinter import ttk
import time
from tkinter import filedialog
from tkinter import filedialog, Tk, Button, Canvas


brush_size = 5



def save_screenshot():
    # Get the canvas widget and its bounding box coordinates
    canvas = canvas_widget
    x, y, width, height = canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_width(), canvas.winfo_height()

    # Capture the canvas area
    screenshot = tk.ImageGrab.grab((x, y, x + width, y + height))

    # Get the user's downloads folder path
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Ask the user for a filename
    file_name = filedialog.asksaveasfilename(initialdir=download_folder, defaultextension=".png")

    # Save the screenshot if a filename is chosen
    if file_name:
        screenshot.save(file_name)
        tk.messagebox.showinfo("Success", f"Screenshot saved to '{file_name}'")

eraser_active = False


# use Antialiasing to blend adjacent pixels to make lines look smoother when the mouse is moved quickly
# according to the tkinter documentation: 
# the value of 'splinesteps' indicates the number of control points to use for spline interpolation, which determines the smoothness of the line.

def paint(event, shade):
    global eraser_active

    if eraser_active:
        # Erase mode: delete any canvas items under the cursor
        x1, y1 = event.x - 2, event.y - 2
        x2, y2 = event.x + 2, event.y + 2
        items = canvas.find_overlapping(x1, y1, x2, y2)
        for item in items:
            canvas.delete(item)
    else:
        # Drawing mode: draw lines
        x1, y1 = (event.x - brush_size), (event.y - brush_size)
        x2, y2 = (event.x + brush_size), (event.y + brush_size)
        canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)

def draw_text(event):
    text = text_entry.get()
    if text:
        font_size = font_size_var.get()
        font = ("Helvetica", font_size, "bold")
        canvas.create_text(event.x, event.y, text=text, fill="black", font=font)

def toggle_eraser():
    global eraser_active
    eraser_active = not eraser_active
    current_color = eraser_button.cget("background")
    new_color = "dark grey" if eraser_active else "SystemButtonFace"
    eraser_button.configure(background=new_color)


def color_picker():
    global shade, current_color
    color = askcolor()
    shade = color[1]
    current_color = shade

def change(shade):
    global current
    current = shade

def clear(canvas):
    '''Clear all drawn objects from the screen'''
    canvas.delete('all')

def update_button_color():
    # Update button color based on eraser mode
    print("Updating button color...")
    eraser_button.configure(bg="grey" if eraser_active else "white")

def update_brush_size(value):
    global brush_size
    brush_size = int(value)

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

# Create the "Eraser" button
eraser_button = tk.Button(root, text="Eraser", command=toggle_eraser)
eraser_button.pack(pady=5)

# Update button color whenever eraser_active changes
eraser_button.bind('<Configure>', update_button_color)

# create the save button
save_button = tk.Button(root, text="Save", command=save_screenshot)
save_button.pack(pady=5)

# adjust brush size 
brush_label = tk.Label(root, text="Brush Size:")
brush_label.pack(side=tk.LEFT, padx=5, pady=5)

brush_size_scale = tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, length=100, command=update_brush_size)
brush_size_scale.set(brush_size)
brush_size_scale.pack(side=tk.LEFT, padx=5, pady=5)

# Create a text entry widget
text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=5)

# Font Size Slider
font_size_var = tk.IntVar()
font_size_var.set(12)  # Default font size

font_size_label = tk.Label(root, text="Font Size:")
font_size_label.pack(pady=5)

font_size_slider = tk.Scale(root, from_=8, to=100, orient=tk.HORIZONTAL, variable=font_size_var)
font_size_slider.pack(pady=5)

# draw text
canvas.bind("<Double-Button-1>", lambda event: draw_text(event))

root.mainloop()