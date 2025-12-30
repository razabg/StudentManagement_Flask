import os
import unittest
from app import blueprint
from app.main import create_app,db
from flask_migrate import Migrate
from app.main.model import student
from app.main.model import student_grade
from app.main.model import user
app = create_app()
app.register_blueprint(blueprint)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# CLI command for running tests
@app.cli.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    app.run(host="0.0.0.0")