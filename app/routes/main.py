from flask import Blueprint, jsonify
from ..services.db_service import get_postgres_version

main = Blueprint('main', __name__)

@main.route('/')
def version():
    version = get_postgres_version()
    return jsonify({"postgres_version by Talha R": version})



