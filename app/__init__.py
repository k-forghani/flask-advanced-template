from flask import Flask
from flask_assets import Environment
import mongoengine as db
from flask_login import LoginManager

def init_app ():
    app = Flask(__name__, instance_relative_config = False)
    app.config.from_object("config.Config")

    db.connect(
        app.config["MONGODB_DB"],
        host = app.config["MONGODB_HOST"],
        port = app.config["MONGODB_PORT"]
    )

    login_manager = LoginManager()
    login_manager.login_view = "panel_bp.login"
    login_manager.login_message = "لطفاً وارد حساب کاربری خود شوید."
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def user_loader (id):
        return User.objects(username = id).first()

    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        from . import commands

        from .assets import compile_static_assets

        from .home import home
        from .panel import panel

        app.register_blueprint(home.home_bp)
        app.register_blueprint(panel.panel_bp)

        compile_static_assets(assets)

        return app