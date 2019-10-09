import os
from app import create_app, db
from app.models import Employer, Position, Task
from flask_migrate import Migrate


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

# shell context
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Employer=Employer, Position=Position, Task=Task)
