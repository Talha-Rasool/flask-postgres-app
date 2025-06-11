
from flask import jsonify
from app import db
from sqlalchemy import text

def get_postgres_version():
    result = db.session.execute(text('SELECT version();'))
    version = result.fetchone()[0]
    return version