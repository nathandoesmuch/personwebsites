from flask import Blueprint, render_template

dayviendunlap = Blueprint('dayviendunlap', __name__)

@dayviendunlap.route("/")
def index():
    return "Hello NathanDoesMuch!"