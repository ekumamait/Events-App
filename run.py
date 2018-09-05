from flask import Flask, jsonify, request, abort, json
from datetime import datetime

app = Flask(__name__)
date = datetime.now()
now = date.strftime("%d-%m-%Y %H:%M")

Users = []

@app.route('/api/add-user', methods=['POST'])
def add_user():
    """ end point to add a user """
    new_user = request.get_json()
    new_user['date'] = now
    Users.append(new_user)
    id = 1
    for user in Users:
        user['user_id'] = id
        id += 1

    return jsonify({'users': Users}), 200

@app.route('/api/all-users', methods=['GET'])
def get_users():
    """ end point for displaying users """
    return jsonify(Users)

@app.route('/api/all-users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """ end point for deleting user """
    for user in Users:
        if user['user_id'] == user_id:
            Users.remove(user)
            return jsonify({'200': 'User removed'}), 400
    return jsonify({'404': 'Resource not found'}), 200

if __name__ == '__main__':
    app.run(debug=True)