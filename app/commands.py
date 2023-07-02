import click
from flask import current_app as app
from flask.cli import AppGroup
from app.models import User

users_cli = AppGroup("users")

@users_cli.command("create-admin")
@click.argument("username")
@click.argument("email")
@click.argument("password")
def create_admin_user (username, email, password):
    if User.objects(username = username).first() is None and User.objects(email = email).first() is None:
        user = User(username = username, email = email, role = "ADMIN")
        user.set_password(password)
        user.save()

app.cli.add_command(users_cli)
