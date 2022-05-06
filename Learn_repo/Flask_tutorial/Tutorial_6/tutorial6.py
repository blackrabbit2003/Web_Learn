#!/usr/bin/env python3

from flask import Flask, redirect, render_template, url_for, request, session,flash
from datetime import timedelta

app = Flask(__name__,template_folder="Template")
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else: 
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))

    return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user = user)
    else:
        flash("You are not login!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash(f"You have been logout! ", "info")
    session.pop("user")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)