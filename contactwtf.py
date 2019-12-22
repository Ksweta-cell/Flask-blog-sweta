from wtforms import StringField, TextAreaField, SubmitField
from wtforms import validators
from flask_wtf import FlaskForm


class ContactForm(FlaskForm):
    email = StringField("Enter Email", validators=[validators.Email()])
    subject = StringField('Enter Subject', validators=[validators.DataRequired()])
    message = TextAreaField("Message", validators=[validators.DataRequired()])
    submit = SubmitField("Submit")
