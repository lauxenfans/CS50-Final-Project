from tkinter import *

root = Tk()
root.title("Four Buttons")

button1 = Button(root, text="Button 1")
button2 = Button(root, text="Button 2")
button3 = Button(root, text="Button 3")
button4 = Button(root, text="Button 4")

frame = Frame(root)
frame.pack(side=BOTTOM, fill=X, expand=True)

button1.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
button2.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
button3.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
button4.pack(side=LEFT, fill=BOTH, padx=5, pady=5)

root.mainloop()
