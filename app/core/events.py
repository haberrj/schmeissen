import functools

from flask import session
from flask_socketio import emit, join_room, leave_room

from app import socketio


def authenticated_only(f):
    # Custom decorator to only allow authenticated users to send data.
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped


@socketio.on('joined', namespace='/game')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit(
        'status',
        {'msg': session.get('name') + ' has joined.'},
        room=room
    )


@socketio.on('text', namespace='/game')
def text(message):
    room = session.get('room')
    emit(
        'message',
        {'msg': session.get('name') + ': ' + message['msg']},
        room=room
    )


@socketio.on('left', namespace='/game')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit(
        'status',
        {'msg': session.get('name') + ' has left.'},
        room=room
    )
