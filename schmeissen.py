#!/usr/bin/python3

import socketio

from app import create_app, db, socketio
from config import DevelopmentConfig


# Remove Config when deploying.
app = create_app(DevelopmentConfig)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
    }


if __name__ == '__main__':
    socketio.run(app)
