#!/usr/bin/env python3
from flask import Flask, render_template, url_for, redirect

app = Flask("__name__", template_folder="Template")

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/test")
def test(): 
    return render_template("new.html")

if __name__ == "__main__":
    app.run(debug=True)