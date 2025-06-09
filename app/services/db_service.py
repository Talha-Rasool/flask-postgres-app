from .. import db

def get_postgres_version():
    result = db.session.execute('SELECT version();')
    return result.fetchone()[0]
