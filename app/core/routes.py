from flask import redirect, render_template, session, url_for
from flask_login import current_user, login_required

from app.core import bp


@bp.route('/')
@bp.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('core.dashboard'))

    return render_template('index.html')


@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('core/dashboard.html')


@bp.route('/game')
@login_required
def game():
    name = current_user.username
    room = 'main'
    session['name'] = name
    session['room'] = room
    return render_template('core/game.html', name=name, room=room)
