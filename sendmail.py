from flask_mail import *
from flask import Flask
import os


app = Flask(__name__)

mail_setting = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['misssweta0786@gmail.com'],
    "MAIL_PASSWORD": os.environ['kumar_ashish@#?123']
}

app.config.update(mail_setting)
mail = Mail(app)
