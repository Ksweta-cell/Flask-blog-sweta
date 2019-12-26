from flask import *


def app1():
    locapp = Flask(__name__)
    locapp.config['SECRET_KEY'] = "ABC"
    locapp.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/universe"

    locapp.config['MAIL_SERVER'] = 'smtp.gmail.com'
    locapp.config['MAIL_PORT'] = 465
    locapp.config['MAIL_USE_SSL'] = True
    locapp.config['MAIL_USE_TLS'] = False
<<<<<<< HEAD
    locapp.config['MAIL_USERNAME'] = 'misssweta0786@gmail.com'
    locapp.config['MAIL_PASSWORD'] = '**********'
=======
    locapp.config['MAIL_USERNAME'] = 'sweta0786@gmail.com'
    locapp.config['MAIL_PASSWORD'] = '********'
>>>>>>> e192d19d3b49655a3137778f5b346b66bdb827bd
    return locapp
