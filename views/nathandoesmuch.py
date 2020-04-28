from flask import Blueprint, render_template

nathandoesmuch = Blueprint('nathandoesmuch', __name__)

@nathandoesmuch.route("/")
def index():
    return render_template('nathandoesmuch.html')