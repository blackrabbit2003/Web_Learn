#!/usr/bin/env python3
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__,template_folder="template")

@app.route("/<name>")
def home(name):
    return render_template("index.html", content=["Tim", "Joe", "Bill"], r=2) 

if __name__ == "__main__":
    app.run(debug=True)
