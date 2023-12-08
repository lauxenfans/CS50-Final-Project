import tkinter as tk
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, Whiteboard
from tkinter import ttk


app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///whiteboard.db")

@app.after_request

def after_request(response):

    """Ensure responses aren't cached"""

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"

    response.headers["Expires"] = 0

    response.headers["Pragma"] = "no-cache"

    return response

 

@app.route("/")

def index():

    return render_template("index.html")

 

if __name__ == "__main__":

    app.run(debug=True)

 

# whiteboard code

@app.route("/whiteboard")

def whiteboard():

    # make and the window, and make it resizable on both axes

    root = tk.Tk()

    root.title("WriteRight - Canvas")

    root.resizable(True, True)

    root.config(background="black")

 

    # make a frame that holds the canvas (and sizegrip!)

    frame = tk.Frame(root)

    frame.pack(fill="both", side=tk.BOTTOM, expand=True)

 

    # make the canvas widget

    canvas = tk.Canvas(frame, bg="white")

    canvas.pack(fill="both", expand=True)

 

    whiteboard_instance = Whiteboard(

        canvas

    )  # Creating an instance of the Whiteboard class

 

    # define what happens when user clicks and drags the left mouse button <B1-Motion>

    # lambda is a keyword for a "throwaway" function that python uses to access a small "anonymous" function

    # got help in office hours for how to use lambda (and also when its no necessary)

    canvas.bind(

        "<B1-Motion>",

        lambda event: whiteboard_instance.paint(event, whiteboard_instance.shade),

    )

    canvas.bind("<Double-Button-1>", lambda event: whiteboard_instance.draw_text(event))

 

    # make the sizegrip element

    sizegrip = ttk.Sizegrip(frame)

    sizegrip.pack(side="bottom", anchor="se")

 

    # make some buttons!

 

    # custom color button

    custom_b = tk.Button(root, text="Color", command=whiteboard_instance.color_picker)

    custom_b.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

 

    # eraser button

    eraser_button = tk.Button(

        root, text="Eraser", command=whiteboard_instance.toggle_eraser

    )

    eraser_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

 

    # a label that shows the brush scale slider

    brush_label = tk.Label(root, text="Brush Size:")

    brush_label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

 

    # the actual brush size adjuster

    brush_size_b = tk.Scale(

        root,

        from_=1,

        to=30,

        orient=tk.HORIZONTAL,

        length=100,

        command=whiteboard_instance.update_brush_size,

    )

    brush_size_b.set(whiteboard_instance.brush_size)

    brush_size_b.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

 

    # text entry

    text_entry = tk.Entry(root, width=30)

    text_entry.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

 

    # font size variable to be adjusted (default 12)

    font_size = tk.IntVar()

    font_size.set(12)

 

    # font size slider

    font_size_slider = tk.Scale(

        root, from_=8, to=100, orient=tk.HORIZONTAL, variable=font_size

    )

    font_size_slider.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

 

    # random drawing button

    random_drawing_b = tk.Button(

        root, text="Random", command=whiteboard_instance.generate_random_drawing

    )

    random_drawing_b.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

 

    # clear button

    clear_b = tk.Button(root, text="Clear", command=whiteboard_instance.clear)

    clear_b.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

 

    # save button

    save_button = tk.Button(

        root, text="Save", command=whiteboard_instance.save_canvas_as_image

    )

    save_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

    # save_canvas_as_image(canvas)

 

    # Create a label to display the eraser message

    eraser_message_label = tk.Label(root, text="", fg="red")

    eraser_message_label.pack(side=tk.LEFT, padx=5, pady=5)

 

    root.mainloop()

 

    return render_template("whiteboard.html")

 

@app.route("/revImageSearch")

def revImageSearch():

    return render_template("layout.html")

 

@app.route("/register", methods=["GET", "POST"])

def register():

    """Register user"""

 

    # User reached route via POST (as by submitting a form via POST)

    if request.method == "POST":

        username = request.form.get("username")

        password = request.form.get("password")

        confirmation = request.form.get("confirmation")

 

        # Ensure username was submitted

        if not username:

            return apology("must provide username", 400)

 

        # Ensure password was submitted

        elif not password:

            return apology("must provide password", 400)

 

        # Ensure confirmation was submitted

        elif not confirmation:

            return apology("must provide password", 400)

 

        # Ensure password and confirmation are the same

        if password != confirmation:

            return apology("must provide password", 400)

 

        # PERSONAL TOUCH!!! Require users’ passwords to have at least 10 characters and must have at least one special character

        if len(password) < 7:

            return apology("password length must be at least 7 characters", 400)

 

        list = ["!", "@", "$", "%", "#", "&"]

        bool = False

 

        for char in password:

            if char in list:

                bool = True

                break

        if bool == False:

            return apology(

                "password must contain AT LEAST ONE special character '!','@','$','%','#','&' ",

                400,

            )

 

        # Check if username in database

        rows = db.execute("SELECT * FROM users WHERE username=?", username)

 

        if len(rows) != 0:

            return apology("username already exists :(", 400)

 

        # Add username to the database

        db.execute(

            "INSERT INTO users (username, hash) VALUES (?, ?)",

            username,

            generate_password_hash(password),

        )

 

        return redirect("/login")

 

    # User reached route via GET (as by clicking a link or via redirect)

    else:

        return render_template("register.html")

 

@app.route("/login", methods=["GET", "POST"])

def login():

    """Log user in"""

 

    # Forget any user_id

    session.clear()

 

    # User reached route via POST (as by submitting a form via POST)

    if request.method == "POST":

        # Ensure username was submitted

        if not request.form.get("username"):

            return apology("must provide username", 403)

 

        # Ensure password was submitted

        elif not request.form.get("password"):

            return apology("must provide password", 403)

 

        # Query database for username

        rows = db.execute(

            "SELECT * FROM users WHERE username = ?", request.form.get("username")

        )

 

        # Ensure username exists and password is correct

        if len(rows) != 1 or not check_password_hash(

            rows[0]["hash"], request.form.get("password")

        ):

            return apology("invalid username and/or password", 403)

 

        # Remember which user has logged in

        session["user_id"] = rows[0]["id"]

 

        # Redirect user to home page

        return redirect("/")

 

    # User reached route via GET (as by clicking a link or via redirect)

    else:

        return render_template("login.html")

 

@app.route("/logout")

def logout():

    """Log user out"""

 

    # Forget any user_id

    session.clear()

 

    # Redirect user to login form

    return redirect("/")