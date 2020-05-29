import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.server_config import ServerConfig

# Flask app
template_dir = os.path.abspath('app/static/webapp')
app = Flask(__name__, template_folder=template_dir)
app.config.from_object(ServerConfig)
'''
refer to - https://itnext.io/how-and-why-have-a-properly-configuration-handling-file-using-flask-1fd925c88f4c
change above line to:
app.config.from_envvar('CONFIGURATION_FILE')
$ export CONFIGURATION_FILE=./config/debug_environment.cfg
'''

# Database setup
db = SQLAlchemy(app)

from app.home.routes import home
app.register_blueprint(home)

from app.user.routes import user
app.register_blueprint(user, url_prefix='/api/users')


print(app.url_map)
