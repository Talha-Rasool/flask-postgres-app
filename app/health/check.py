# app/health/check.py
from flask import Blueprint, jsonify

health = Blueprint("health", __name__)

@health.route("/healthz", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@health.route("/readiness", methods=["GET"])
def readiness_check():
    # Optionally check DB connection or dependencies here
    return jsonify({"ready": True}), 200
