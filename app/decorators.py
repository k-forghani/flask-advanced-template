from flask import current_app as app
from flask_login import current_user
from functools import wraps

def login_required (role = "ANY"):
    def wrapper (fn):
        @wraps(fn)
        def decorated_view (*args, **kwargs):
            if not current_user.is_authenticated:
               return app.login_manager.unauthorized()
            if current_user.role != role and role != "ANY":
                return app.login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
