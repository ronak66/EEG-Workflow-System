from flask import Blueprint, request, Response, make_response, jsonify

from app.user.controller import user_login

user = Blueprint('user', __name__)

@user.route("/login", methods=["POST"])
def login_user():
    return user_login()