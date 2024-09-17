"""app00/forms.py"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """LoginForm"""

    email = StringField(
        "Email",
        validators=[
            DataRequired(message="必須項目です"),
            Email(message="正しいメールアドレスを入力してください"),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
