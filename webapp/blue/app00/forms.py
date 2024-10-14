"""app00/forms.py"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """LoginForm"""

    email = StringField(
        "Email",
        validators=[
            DataRequired(message="This field is required."),
            Email(message="Please enter a valid email address."),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
