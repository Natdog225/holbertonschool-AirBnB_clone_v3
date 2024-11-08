^#!/usr/bin/python3
"""Index file for reasons"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """I know it seems crazy, but this defines the status of API"""
    return jsonify({"status": "OK"})