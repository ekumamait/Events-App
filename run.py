from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/api/add-user', methods=['POST'])
def add_user():
    """ end point to add a user """
    if request.methods != "POST":
        abort(405)

    return jsonify({}), 200

@app.route('/api/get-users', methods=['GET'])
def get_users():
    """ end point for displaying users """
    if request.methods != "GET":
        abort(405)

    return jsonify({})

@app.route('/api/delete-user', methods=['DELETE'])
def delete_user():
    """ end point for deleting user """
    if request.methods != "DELETE":
        abort(405)

    return jsonify({}), 200

if __name__ == '__main__':
    app.run(debug=True)