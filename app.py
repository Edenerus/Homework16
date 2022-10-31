from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from utils import *
from classes import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route("/users", methods=["GET"])
def get_users():
    result = []
    for user in User.query.all():
        result.append(user.to_dict())

        return jsonify(result)

if __name__ == '__main__':
    init_database()
    app.run(debug=True)

