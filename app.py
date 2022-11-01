import json

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from utils import init_database
from classes import User, Order, Offer
from db import app


@app.route("/users", methods=["GET", "POST"])
def get_users():
    if request.method == "GET":

        result = []
        users = User.query.all()
        for user in users:

            result.append(user.to_dict())

        return jsonify(result), 200

    if request.method == "POST":
        user_data = json.loads(request.data)

        db.session.add(
            User(
                id=user_data.get("id"),
                first_name=user_data.get("first_name"),
                last_name=user_data.get("last_name"),
                age=user_data.get("age"),
                email=user_data.get("email"),
                role=user_data.get("role"),
                phone=user_data.get("phone"),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def get_user_id(id):
    if request.method == "GET":
        user = User.query.get(id).to_dict()

        return jsonify(user), 200

    if request.method == "PUT":
        user_data = json.loads(request.data)
        user = User.query.get(id)

        user.first_name = user_data["first_name"]
        user.last_name = user_data["last_name"]
        user.age = user_data["age"]
        user.email = user_data["email"]
        user.role = user_data["role"]
        user.phone = user_data["phone"]

        db.session.add(user)
        db.session.commit

        return "", 201

    if request.method == "DELETE":
        user = User.query.get(id)

        db.session.delete(user)
        db.session.commit()

        return "", 204


@app.route("/orders", methods=["GET", "POST"])
def get_orders():
     if request.method == "GET":

        result = []
        orders = Order.query.all()
        for order in orders:
            result.append(order.to_dict())

        return jsonify(result), 200

     if request.method == "POST":
         order_data = json.loads(request.data)

         db.session.add(
             Order(
                 id=order_data.get("id"),
                 name=order_data.get("name"),
                 description=order_data.get("description"),
                 start_date=order_data.get("start_date"),
                 end_date=order_data.get("end_date"),
                 address=order_data.get("address"),
                 price=order_data.get("price"),
                 customer_id=order_data.get("customer_id"),
                 executor_id=order_data.get("executor_id"),
             )
         )
         db.session.commit()

         return "", 201


@app.route("/orders/<int:id>", methods=["GET", "PUT", "DELETE"])
def get_order_id(id):
    if request.method == "GET":
        order = Order.query.get(id).to_dict()

        return jsonify(order), 200

    if request.method == "PUT":
        order_data = json.loads(request.data)
        order = Order.query.get(id)

        order.name = order_data["name"]
        order.description = order_data["description"]
        order.start_date = order_data["start_date"]
        order.end_date = order_data["end_date"]
        order.address = order_data["address"]
        order.price = order_data["price"]
        order.customer_id = order_data["customer_id"]
        order.executor_id = order_data["executor_id"]

        db.session.add(user)
        db.session.commit

        return "", 201

    if request.method == "DELETE":
        order = Order.query.get(id)

        db.session.delete(order)
        db.session.commit()

        return "", 204


@app.route("/offers", methods=["GET", "POST"])
def get_offers():
    if request.method == "GET":

        result = []
        offers = Offer.query.all()
        for offer in offers:
            result.append(offer.to_dict())

        return jsonify(result), 200

    if request.method == "POST":
        offer_data = json.loads(request.data)

        db.session.add(
            Offer(
                id=offer_data.get("id"),
                order_id=offer_data.get("order_id"),
                executor_id=offer_data.get("executor_id"),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/offers/<int:id>", methods=["GET", "PUT", "DELETE"])
def get_offer_id(id):
    if request.method == "GET":
        offer = Offer.query.get(id).to_dict()

        return jsonify(offer), 200

    if request.method == "PUT":
        offer_data = json.loads(request.data)
        offer = Offer.query.get(id)

        offer.order_id = offer_data["order_id"]
        offer.executor_id = offer_data["executor_id"]

        db.session.add(offer)
        db.session.commit

        return "", 201

    if request.method == "DELETE":
        offer = Offer.query.get(id)

        db.session.delete(offer)
        db.session.commit()

        return "", 204


if __name__ == '__main__':
    init_database()
    app.run(debug=True)
