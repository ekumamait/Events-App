from flask import Flask, Request, json, jsonify, Blueprint
from main import students

app = Flask(__name__)

studentsBlueprint = Blueprint(__name__,'students')
app.register_blueprint(studentsBlueprint)    

if __name__ == "__main__":
    app.run(debug=True)










    