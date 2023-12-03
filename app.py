import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        "layout.html")

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/whiteboard')
def whiteboard():
    return render_template(
            "layout.html")


@app.route('/history')
def history():
    return render_template(
        "layout.html")

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

        return redirect("/")

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