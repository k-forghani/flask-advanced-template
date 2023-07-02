from flask import Blueprint
from flask import current_app as app
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.decorators import login_required
from app.models import User
from app.forms import SignupForm, LoginForm

panel_bp = Blueprint(
    "panel_bp", __name__,
    url_prefix = "/panel",
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "/static/panel"
)

@panel_bp.route("/signup", methods = ["GET", "POST"])
def signup ():
    if current_user.is_authenticated:
        return redirect(url_for("home_bp.home"))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        user.save()
        flash("تبریک، شما هم‌اکنون یک حساب کاربری در وب‌سایت دارید!")
        return redirect(url_for("panel_bp.login"))
    return render_template(
        "signup.jinja2",
        title = "میزان",
        subtitle = "قالبی پیشرفته و متن‌باز برای فلسک",
        form = form,
        page = "signup"
    )

@panel_bp.route("/login", methods = ["GET", "POST"])
def login ():
    if current_user.is_authenticated:
        return redirect(url_for("home_bp.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("نام کاربری یا گذرواژه نامعتبر است.")
            return redirect(url_for("panel_bp.login"))
        login_user(user, remember = form.remember_me.data)
        return redirect(url_for("home_bp.home"))
    return render_template(
        "login.jinja2",
        title = "میزان",
        subtitle = "قالبی پیشرفته و متن‌باز برای فلسک",
        form = form,
        page = "login"
    )

@panel_bp.route("/logout")
@login_required(role = "ANY")
def logout ():
    logout_user()
    return redirect(url_for("home_bp.home"))
