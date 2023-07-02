from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length, Email
from app.models import User

class SignupForm (FlaskForm):
    username = StringField("نام کاربری", validators = [
        DataRequired(message = "لطفاً یک نام کاربری وارد نمایید."),
        Length(min = 4, max = 25, message = "نام کاربری باید میان ۴ تا ۲۵ کاراکتر طول داشته باشد.")
    ])
    email = StringField("پست الکترونیک", validators = [
        DataRequired(message = "لطفاً یک پست الکترونیک وارد نمایید."),
        Email(message = "پست الکترونیک معتبر نیست.")
    ])
    password = PasswordField("گذرواژه", validators = [
        DataRequired(message = "لطفاً یک گذرواژه وارد نمایید."),
        Length(min = 8, message = "گذرواژه باید حداقل ۸ کاراکتر طول داشته باشد."),
        EqualTo("confirm", message = "گذرواژه‌های وارد شده با هم منطبق نیستند.")
    ])
    confirm = PasswordField("تکرار گذرواژه", validators = [
        DataRequired(message = "تکرار گذرواژه نمی‌تواند خالی باشد.")
    ])
    accept_tos = BooleanField("قوانین و مقررات وب‌سایت را می‌پذیرم.", validators = [
        DataRequired(message = "استفاده از سرویس‌های وب‌سایت بدون پذیرش قوانین و مقررات حاکم بر آن امکان‌پذیر نیست.")
    ])
    submit = SubmitField("تأیید اطلاعات ثبت‌نام")

    def validate_username (self, username):
        user = User.objects(username = username.data).count()
        if user != 0:
            raise ValidationError("نام کاربری قبلاً مورد استفاده قرار گرفته است.")

    def validate_email (self, email):
        user = User.objects(email = email.data).count()
        if user != 0:
            raise ValidationError("قبلاً یک حساب کاربری با این پست الکترونیک ایجاد شده است.")

class LoginForm (FlaskForm):
    username = StringField("نام کاربری", validators = [
        DataRequired(message = "لطفاً نام کاربری خود را وارد نمایید.")
    ])
    password = PasswordField("گذرواژه", validators = [
        DataRequired(message = "لطفاً گذرواژه خود را وارد نمایید.")
    ])
    remember_me = BooleanField("مرا به‌خاطر بسپار")
    submit = SubmitField("ورود")
