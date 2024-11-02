"""__init__.py"""

from datetime import timedelta
from flask import Flask, render_template, session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object("webapp.config")

# Flask-SQLAlchemy
db = SQLAlchemy(app)

# Flask-Migrate
migrate = Migrate(app, db)

# Flask-Admin
admin = Admin(app, name="App Admin", template_mode="bootstrap4")

# Flask-Login
login_manager = LoginManager()
login_manager.login_view = "app00.login"
login_manager.init_app(app)

# app00
from webapp.blue.app00.views import app00  # pylint: disable=C0413
from webapp.blue.app00.models import User, UserLoginHistory  # pylint: disable=C0413
from webapp.blue.app00.admin import (  # pylint: disable=C0413
    UserModelView,
    UserLoginHistoryModelView,
)

app.register_blueprint(app00)
admin.add_view(UserModelView(User, db.session))
admin.add_view(UserLoginHistoryModelView(UserLoginHistory, db.session))


@login_manager.user_loader
def load_user(user_id):
    """load_user"""
    try:
        return User.query.get(int(user_id))
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """before_request"""
    session.permanent = True
    app.permanent_session_lifetime = timedelta(hours=2)
    session.modified = True


@app.route("/", methods=["GET", "POST"])
def home():
    """home"""
    return render_template("home.html")
