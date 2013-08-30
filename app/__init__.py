from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
UPLOAD_FOLDER = '/home/mykyta.morachov/PycharmProjects/Outpost/app/static/img'
EXPORTS_URL = '/static/exports'
EXPORTS_FOLDER = '/home/mykyta.morachov/PycharmProjects/Outpost/app/static/exports'
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'gif', 'jpeg'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/outpost'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Vakoms4ever!@localhost/thatriff'
#app.secret_key = "\xa7\xab\x87\xd7\xff\xdc\xae \x0cY\x87\xf9t\xea\x19\t\x0eN\xe9\xea\xe8\xb6\xd6>"
db = SQLAlchemy(app)

from app import views