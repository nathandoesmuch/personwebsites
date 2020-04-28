# coding=utf-8
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    if request.host == 'nathandoesmuch.com':
        return render_template("nathandoesmuch.html")
    elif request.host == 'victoriashakes.com':
        return "Hello, Victoria!"
    elif request.host == 'tybarr.com.com':
        return "Hello, Ty!"
    elif request.host == 'dayviendunlap.com':
        return "Hello, Dayvien!"
    else:
        return "Hello, Other users!"

if __name__ == "__main__":
    app.run()
