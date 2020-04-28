# coding=utf-8
from flask import Flask, render_template
from views.nathandoesmuch import nathandoesmuch
from views.victoriashakes import victoriashakes
from views.tybarr import tybarr
from views.dayviendunlap import dayviendunlap

app = Flask(__name__, host_matching=True, static_host='nathandoesmuch.com')

app.register_blueprint(nathandoesmuch, host='nathandoesmuch.com')
app.register_blueprint(victoriashakes, host='victoriashakes.com')
app.register_blueprint(tybarr, host='tybarr.com')
app.register_blueprint(dayviendunlap, host='dayviendunlap.com')

if __name__ == "__main__":
    app.run()
