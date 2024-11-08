#!/usr/bin/python3
from os import abort
from urllib import request
from api.v1.views import app_views
from models.user import User
from flask import Flask, jsonify

@app_views.route('/users', methods=['GET'])
def get_users():
    """
    Retrieves the list of all User objects.
    """
    users = User.all()
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieves a User object by its ID.
    """
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users', methods=['POST'])
def create_user():
    """
    Creates a new User object.
    """
    data = request.get_json()
    if not data:
        abort(400, message="Missing data")
    required_fields = ["email", "password"]
    for field in required_fields:
        if field not in data:
            abort(400, message=f"Missing field: {field}")
    user = User(email=data["email"], password=data["password"])
    user.save()
    return jsonify(user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Updates a User object by its ID.
    """
    user = User.get(user_id)
    if user is None:
        abort(404)
    data = request.get_json()
    if data:
        for key, value in data.items():
            if key not in ["id", "email", "created_at", "updated_at"]:
                setattr(user, key, value)
        user.save()
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a User object by its ID.
    """
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.delete()
    return jsonify({})