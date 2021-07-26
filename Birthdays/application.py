import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)Birthd

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():

    # Add the user's entry into the database
    if request.method == "POST":

        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Add info to birthdays datatable (remember that '?' is a placeholder)
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        return redirect("/")

    # Display the entries in the database on index.html
    else:
        # Store datatable in registrants variable
        registrants = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", registrants=registrants)


