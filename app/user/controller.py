import json
from flask import Response, make_response, jsonify

def user_login():
    json_format = jsonify(
        {
            'reset': False,
            'id': -1, 
            'email': 'test5', 
            'token': 'guest'
        }
    )
    return json_format