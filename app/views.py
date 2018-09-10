from flask import Flask, jsonify, request, abort, json
from datetime import datetime
from app import app
from app.models import Users, Events, Tickets

tck = Tickets()
db = Events()
bd = Users()
app = Flask(__name__)
date = datetime.now()
now = date.strftime("%d-%m-%Y %H:%M")

@app.route('/api/add-user', methods=['POST'])
def add_user():
    """ end point to add a user """
    
    new_user = request.get_json()
    bd.insert_new_user(new_user['first_name'], new_user['last_name'], new_user['age'], new_user['user_email'], new_user['user_password'], new_user['date'])
    return jsonify({'users': Users}), 200

@app.route('/api/all-users', methods=['GET'])
def get_events():
    """ end point for displaying users """
    event = db.get_all_events(event_id)
    return jsonify(Users)

@app.route('/api/v2/events/<int:event_id>', methods = ['GET'])
def single_event(user_id, event_id):
    """ end point for displaying a single event """
    if request.method != "GET":
        abort(405)

    event = db.get_event_by_id(user_id, event_id)
    return jsonify({'event': event})

@app.route('/api/v2/events', methods = ['POST'] )
def add_event(user_id):
    """  end point to add an event """
    if request.method != "POST":
        abort(405)

    event = request.get_json()
    event['date'] = now
    db.insert_new_event(event[''], event['location'], event['date'], user_id)
    return jsonify({'msg': 'new event added'}), 200

if __name__ == '__main__':
    app.run(debug=True)