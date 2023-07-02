from flask import current_app as app
from flask_assets import Bundle

def compile_static_assets (assets):
    assets.auto_build = True
    assets.debug = False

    bundles = {
        "framework_css": Bundle(
            "src/css/bootstrap.rtl.css",
            # filters = "cssmin",
            output = "dist/css/framework.css",
            extra = {"rel": "stylesheet/css"}
        ),
        "framework_js": Bundle(
            "src/js/bootstrap.bundle.js",
            filters = "jsmin",
            output = "dist/js/framework.js"
        ),
        "main_css": Bundle(
            "src/css/main.css",
            # filters = "cssmin",
            output = "dist/css/main.css",
            extra = {"rel": "stylesheet/css"}
        ),
        "main_js": Bundle(
            "src/js/main.js",
            filters = "jsmin",
            output = "dist/js/main.js"
        ),
        "fonts_css": Bundle(
            "src/css/fonts.css",
            # filters = "cssmin",
            output = "dist/css/fonts.css",
            extra = {"rel": "stylesheet/css"}
        ),
        "home_css": Bundle(
            "home_bp/css/home.css",
            # filters = "cssmin",
            output = "dist/css/home.css",
            extra = {"rel": "stylesheet/css"}
        )
    }

    assets.register(bundles)

    if app.config["FLASK_ENV"] == "development":
        for bundle in bundles.values():
            bundle.build()

    return assets