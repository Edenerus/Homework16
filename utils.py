import json
from classes import *
from db import db
from app import app


def get_users_all(path="data/users.json"):

    with open(path, 'r', encoding='utf-8') as file:
        users = json.load(file)

    return users


def get_users_all(path="data/users.json"):

    with open(path, 'r', encoding='utf-8') as file:
        users = json.load(file)

    return users


def get_offers_all(path='data/offers.json'):

    with open(path, 'r', encoding='utf-8') as file:
        offers = json.load(file)

    return offers


def get_orders_all(path='data/orders.json'):

    with open(path, 'r', encoding='utf-8') as file:
        orders = json.load(file)

    return orders


def init_database():
    app.app_context().push()
    db.drop_all()
    db.create_all()

    for user_data in get_users_all():
        new_user = User(
            id=user_data.get("id"),
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            age=user_data.get("age"),
            email=user_data.get("email"),
            role=user_data.get("role"),
            phone=user_data.get("phone"),
        )

        db.session.add(new_user)
        db.session.commit()


    for order_data in get_orders_all():
        new_order = Order(
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

        db.session.add(new_order)
        db.session.commit()


    for offer_data in get_offers_all():
        new_offer = Offer(
            id=offer_data.get("id"),
            order_id=offer_data.get("order_id"),
            executor_id=offer_data.get("executor_id"),
        )

        db.session.add(new_offer)
        db.session.commit()
