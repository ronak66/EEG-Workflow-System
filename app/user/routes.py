import json
from flask import Blueprint, request, Response, make_response, jsonify

from app.user.controller import user_login, create_new_user, change_password

user = Blueprint('user', __name__)

@user.route("/login", methods=["POST"])
def login_user():
    try:
        data = request.form
        return user_login(data)
    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': e}),
            status=400
        )        



@user.route("/register", methods=["POST"])
def user_register():
    try:
        data = request.form
        return create_new_user(data)
    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': e}),
            status=400
        )

@user.route("/reset", methods=["POST"])
def reset_password():
    try:
        data = request.form
        return change_password(data)
    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': e}),
            status=400
        )