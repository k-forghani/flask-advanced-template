from flask import Blueprint
from flask import current_app as app
from flask import render_template

home_bp = Blueprint(
    "home_bp", __name__,
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "/static/home"
)

@home_bp.route("/", methods = ["GET"])
def home ():
    return render_template(
        "index.jinja2",
        title = "میزان",
        subtitle = "قالبی پیشرفته و متن‌باز برای فلسک",
        page = "home"
    )