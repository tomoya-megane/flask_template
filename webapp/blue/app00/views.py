"""app00/views.py"""

from urllib.parse import urlparse
import logging
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user, current_user

from webapp.blue.app00.models import User, UserLoginHistory
from webapp.blue.app00.forms import LoginForm
from webapp import db

app00 = Blueprint("app00", __name__, template_folder="templates")


@app00.route("/login/", methods=["GET", "POST"])
def login():
    """login"""
    if current_user.is_authenticated:
        next_page = request.args.get("next")
        if not next_page or urlparse(next_page).netloc != "":
            next_page = url_for("home")
        return redirect(next_page)

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("メールアドレスまたはパスワードが間違っています。", "danger")
        else:
            login_user(user)
            login_history = UserLoginHistory(
                user_id=user.id,
                ip_address=request.remote_addr,
                user_agent=request.headers.get("User-Agent"),
            )
            try:
                db.session.add(login_history)
                db.session.commit()
                flash("ログイン成功", "success")
            except Exception as e:  # pylint: disable=W0703
                db.session.rollback()
                logging.error("Database error occurred: %s", e)
                flash("データベースエラーが発生しました。", "danger")
            return redirect(url_for("home"))

    return render_template("login.html", form=form)


@app00.route("/logout/")
@login_required
def logout():
    """logout"""
    logout_user()
    flash("ログアウトしました。", "success")
    return redirect(url_for("app00.login"))
