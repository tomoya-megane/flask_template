"""app00/admin.py"""

from urllib.parse import urlparse
import logging
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, request


# AdminModelView
class AdminModelView(ModelView):
    """AdminModelView"""

    def is_accessible(self):
        if not current_user.is_authenticated or not current_user.is_admin:
            logging.warning(
                "Unauthorized access attempt by %s",
                current_user.email if current_user.is_authenticated else "Anonymous",
            )
            return False
        return True

    def inaccessible_callback(self, name, **kwargs):
        next_url = request.url
        if not next_url or urlparse(next_url).netloc != "":
            next_url = url_for("home")
        return redirect(url_for("app00.login", next=next_url))


# UserModelView
class UserModelView(AdminModelView):
    """UserModelView"""

    column_list = ("id", "email", "is_admin", "password_hash")

    column_labels = {
        "id": "User ID",
        "email": "User Email",
        "is_admin": "Administrator",
        "user_agent": "Password Hash",
    }


# UserLoginHistoryModelView
class UserLoginHistoryModelView(AdminModelView):
    """UserLoginHistoryModelView"""

    column_list = (
        "id",
        "user_id",
        "user.email",
        "login_time",
        "ip_address",
        "user_agent",
    )

    column_labels = {
        "id": "Log ID",
        "user_id": "User ID",
        "user.email": "User Email",
        "login_time": "Login Time",
        "ip_address": "IP Address",
        "user_agent": "User Agent",
    }

    column_auto_select_related = True
