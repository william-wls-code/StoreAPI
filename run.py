from app import app
from db import db

'''
If uWSGI is used, since it does not run app.py file, the line:
    if __name__ == '__main__':
never runs. Furthermore, since db is not imported, the create_tables() function never runs.

Therefore, in order to prevent this problem and circular imports, this file, run.py, is created. Also, the setting in uwsgi.ini is changed from 'module = app:app' to 'module = run:app'.
'''

db.init_app(app)


@app.before_first_request
def create_tables():
    ''' Create the tables before the first request. '''
    db.create_all()
