import json
from flask import Response, make_response, jsonify, g

from app import db, bcrypt
from app.user.auth import Auth
from app.user.model import User

def user_login(data):
    try:
        print("="*80,"Logging User:",sep="\n")
        user = User.get_user_via_email(data['email'])
        if(user and user.check_hash_password(data['password'])):
            token = Auth.generate_token(user.id)
            response = {
                'reset': False,
                'id': str(user.id), 
                'email': str(user.email),
                'token': str(token),
                'username': str(user.username)
            }
            # res = make_response(jsonify(response))
            print(token)
            print("Login Sucess","="*80,sep="\n")
            # res.set_cookie(key="session", value=token, domain="eeg-workflow.herokuapp.com", max_age=None)
            return Response(
                mimetype="application/json",
                response=json.dumps(response),
                status=200
            )
            # return res, 200, {'Content-Type': 'application/json'}
        else:
            print("Wrong Password","="*80,sep="\n")
            return Response(
                mimetype="application/json",
                response=json.dumps({'error': 'Error with your e-mail/password combination'}),
                status=403
            )
    except Exception as e:
        print("Error: {}".format(e))
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': str(e)}),
            status=400
        )

def create_new_user(data):
    try:
        print("="*80,"Creating New User:",sep="\n")
        user = User.get_user_via_email(data['email'])
        if(user):
            print("User already exists")
            print("="*80)
            return Response(
                mimetype="application/json",
                response=json.dumps({'error': 'user exsists'}),
                status=403
            )
        hashed_password = User.generate_hash_password(data['password'])
        new_user = User(username=data['username'], email=data['email'], password=hashed_password)
        new_user.save()
        print("New User Created","="*80,sep="\n")
        return Response(
            mimetype="application/json",
            response=json.dumps({'success': "New User Created"}),
            status=201
        )
    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': str(e)}),
            status=400
        )

@Auth.auth_required
def change_password(data):
    try:
        print("="*80,"Changing Password",sep="\n")
        user_id = g.user['id']
        user = User.query.get(user_id)
        if(user and user.check_hash_password(data['currentPassword'])):
            new_hashed_password = User.generate_hash_password(data['newPassword'])
            user.password = new_hashed_password
            user.commit()
            print("Password Changed","="*80,sep="\n")
            return Response(
                mimetype="application/json",
                response=json.dumps({'success': 'Password Changed'}),
                status=200
            )
        else:
            print("Incorrect Password","="*80,sep="\n")
            return Response(
                mimetype="application/json",
                response=json.dumps({'error': 'Incorrect Password'}),
                status=403
            )
    except Exception as e:
        return Response(
                mimetype="application/json",
                response=json.dumps({'error': str(e)}),
                status=400
            )