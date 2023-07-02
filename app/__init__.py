from flask import Flask
from flask_assets import Environment

def init_app ():
    app = Flask(__name__, instance_relative_config = False)
    app.config.from_object("config.Config")

    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        from .assets import compile_static_assets

        from .home import home

        app.register_blueprint(home.home_bp)

        compile_static_assets(assets)

        return app