# testing 
print("testing")

print("hello sava")

print("bob")

import tkinter as tk

root = tk.Tk()

def do_stuff():
    if button.cget('bg') == 'tomato':   # Check current color
        button.config(bg='powder blue', activebackground='powder blue')
    # Do other stuff if you want

button = tk.Button(root, text='Change color', command=do_stuff, 
                   bg='tomato', activebackground='tomato')
button.pack(padx=50, pady=20)

root.mainloop()