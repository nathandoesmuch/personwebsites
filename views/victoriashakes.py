from flask import Blueprint, render_template

victoriashakes = Blueprint('victoriashakes', __name__)

@victoriashakes.route("/")
def index():
    return "Hello Victoria!"