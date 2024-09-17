"""app00/models.py"""

from datetime import datetime
from zoneinfo import ZoneInfo
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp import db


# User
class User(UserMixin, db.Model):
    """User"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        """set_password"""
        self.password_hash = generate_password_hash(
            password, method="pbkdf2:sha256", salt_length=16
        )

    def check_password(self, password):
        """check_password"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User id={self.id}, email={self.email}, is_admin={self.is_admin}>"


# UserLoginHistory
class UserLoginHistory(db.Model):
    """UserLoginHistory"""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    login_time = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(ZoneInfo("UTC"))
    )
    ip_address = db.Column(db.String(50))
    user_agent = db.Column(db.String(500))

    user = db.relationship(
        "User", backref=db.backref("login_histories", lazy="dynamic")
    )

    def __repr__(self):
        return (
            f"<LoginHistory user_id={self.user_id}, "
            f"login_time={self.login_time}, "
            f"ip_address={self.ip_address}>"
        )
