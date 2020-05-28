from flask import Blueprint, request, Response, make_response, render_template

home = Blueprint('home', __name__)

@home.route("/", methods=["GET"])
def login_user():
    return render_template('index.html')