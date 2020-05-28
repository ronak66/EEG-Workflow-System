import json
from flask import Blueprint, request, Response, make_response, jsonify

user = Blueprint('user', __name__)

@user.route("/login", methods=["POST"])
def login_user():
    a = jsonify({'reset': False, 'id': -1, 'email': 'test5', 'token': 'guest'})
    print("="*80)
    print(a)
    print("="*80)
    return a