import jwt
import json
import datetime
from functools import wraps
from flask import Response, request, g

from app.user.model import User
from app.server_config import ServerConfig

class Auth():
    """
    Auth Class
    """
    @staticmethod
    def generate_token(user_id):
        """
        Generate Token Method
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=2),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                ServerConfig.JWT_SECRET_KEY,
                'HS256'
            ).decode("utf-8")
        except Exception as e:
            return Response(
                mimetype="application/json",
                response=json.dumps({'error': 'error in generating user token'}),
                status=400
            )

    @staticmethod
    def decode_token(token):
        """
        Decode token method
        """
        re = {'data': {}, 'error': {}}
        try:
            payload = jwt.decode(token, ServerConfig.JWT_SECRET_KEY)
            re['data'] = {'user_id': payload['sub']}
            return re
        except jwt.ExpiredSignatureError as e1:
            re['error'] = {'message': 'token expired, please login again'}
            return re
        except jwt.InvalidTokenError:
            re['error'] = {'message': 'Invalid token, please try again with a new token'}
            return re

    # decorator
    @staticmethod
    def auth_required(func):
        """
        Auth decorator
        """
        @wraps(func)
        def decorated_auth(*args, **kwargs):
            if 'token' not in request.cookies:
                return Response(
                    mimetype="application/json",
                    response=json.dumps({'error': 'Authentication token is not available, please login to get one'}),
                    status=403
                )
            token = request.cookies.get('token')
            data = Auth.decode_token(token)
            if data['error']:
                return Response(
                    mimetype="application/json",
                    response=json.dumps(data['error']),
                    status=400
                )
                
            user_id = data['data']['user_id']
            check_user = User.query.get(user_id)
            if not check_user:
                return Response(
                    mimetype="application/json",
                    response=json.dumps({'error': 'user does not exist, invalid token'}),
                    status=404
                )
            print("-"*80)
            print("api-token: {}".format(token))
            print("user: {}".format(check_user))
            print("-"*80)
            g.user = {'id': user_id}
            return func(*args, **kwargs)
        return decorated_auth
