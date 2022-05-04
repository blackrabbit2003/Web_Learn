# Tutorial #1: How to Make Websites with Python
----
## Source code:
```python
#!//usr/bin/env python3
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home(): 
    return "Hello This is the main page! <h1>HELLO<h1>"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/<name>")
def user(name):
    return f"Hello {name}! "

if  __name__ == "__main__": 
    app.run()
``` 