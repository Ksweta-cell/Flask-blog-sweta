from flask import *


def app1():
    locapp = Flask(__name__)
    locapp.config['SECRET_KEY'] = "ABC"
    locapp.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/universe"

    locapp.config['MAIL_SERVER'] = 'smtp.gmail.com'
    locapp.config['MAIL_PORT'] = 465
    locapp.config['MAIL_USE_SSL'] = True
    locapp.config['MAIL_USE_TLS'] = False
    locapp.config['MAIL_USERNAME'] = 'sweta0786@gmail.com'
    locapp.config['MAIL_PASSWORD'] = '********'
    return locapp
