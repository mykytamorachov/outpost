
from app import app
from models import *

@app.route('/')
@app.route('/index')
def index():
    print "safds"
    object = Object.query.all()
    print dir(object)
    return "Hello, World!"