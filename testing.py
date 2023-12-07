import pyautogui
import tkinter as tk

root= tk.Tk()

# Define tkinter window 
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

# Define fuction to take screenshot
def takeScreenshot ():
    
    x, y = canvas1.winfo_rootx(), canvas1.winfo_rooty()
    w, h = canvas1.winfo_width(), canvas1.winfo_height()
    pyautogui.screenshot('screenshot.png', region=(x, y, w, h))

# Define fuction to take screenshot
myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green',fg='white',font= 10)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()