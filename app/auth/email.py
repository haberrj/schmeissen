from flask import current_app, render_template
from flask_babel import _

from app.email import send_email


def send_password_reset_email(user):
    token = user.get_password_reset_token()
    send_email(_('[Schmeissen] Please reset your password'),
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               html_body=render_template('email/password_reset.html',
                                         user=user, token=token))