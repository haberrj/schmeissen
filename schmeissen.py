from app import create_app, db
from config import DevelopmentConfig, StagingConfig


# Remove Config when deploying.
app = create_app(DevelopmentConfig)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
    }
