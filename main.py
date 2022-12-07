import json
import functions
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# ______Создание классов______


class Offer(db.Model):
    __tablename__ = "offer"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    start_date = db.Column(db.String(30))
    end_date = db.Column(db.String(30))
    address = db.Column(db.String(150))
    price = db.Column(db.Float)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    email = db.Column(db.String(40))
    role = db.Column(db.String(40))
    phone = db.Column(db.String(40))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


# ______Добавление данных в СУБД______


with app.app_context():
    db.create_all()

    users_list = functions.open_users()
    for user in users_list:
        new_user = User(
            id=user["id"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            age=user["age"],
            email=user["email"],
            role=user["role"],
            phone=user["phone"]
        )

        db.session.add(new_user)
        db.session.commit()

    orders_list = functions.open_orders()
    for order in orders_list:
        new_order = Order(
            id=order["id"],
            name=order["name"],
            description=order["description"],
            start_date=order["start_date"],
            end_date=order["end_date"],
            address=order["address"],
            price=order["price"],
            customer_id=order["customer_id"],
            executor_id=order["executor_id"]
        )
        db.session.add(new_order)
        db.session.commit()

    offers_list = functions.open_offers()
    for offer in offers_list:
        new_offer = Offer(
            id=offer["id"],
            order_id=offer["order_id"],
            executor_id=offer["executor_id"]
        )

        db.session.add(new_offer)
        db.session.commit()


# ______Представления______


@app.route("/users", methods=["GET", "POST"])
def all_users():

    if request.method == "GET":
        result = []
        for user in User.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200

    elif request.method == "POST":
        new_user = json.loads(request.data)
        user_data = User(
            id=new_user["id"],
            first_name=new_user["first_name"],
            last_name=new_user["last_name"],
            age=new_user["age"],
            email=new_user["email"],
            role=new_user["role"],
            phone=new_user["phone"]
        )
        db.session.add(user_data)
        db.session.commit()
        return f"New user is added to database", 201


@app.route("/users/<id>", methods=["GET", "PUT", "DELETE"])
def user_by_id(id):
    if request.method == "GET":
        return jsonify(User.query.get(id).to_dict()), 200
    elif request.method == "PUT":
        new_user = json.loads(request.data)
        user = User.query.get(id)
        user.first_name = new_user["first_name"]
        user.last_name = new_user["last_name"]
        user.age = new_user["age"]
        user.email = new_user["email"]
        user.role = new_user["role"]
        user.phone = new_user["phone"]

        db.session.add(user)
        db.session.commit()
        return f"User {id} is updated", 204

    elif request.method == "DELETE":
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return f"User {id} is deleted", 204


@app.route("/orders", methods=["GET", "POST"])
def all_orders():
    if request.method == "GET":
        result = []
        for order in Order.query.all():
            result.append(order.to_dict())
        return jsonify(result), 200

    elif request.method == "POST":
        new_order = json.loads(request.data)
        order_data = Order(
            id=new_order["id"],
            name=new_order["name"],
            description=new_order["description"],
            start_date=new_order["start_date"],
            end_date=new_order["end_date"],
            address=new_order["address"],
            price=new_order["price"],
            customer_id=new_order["customer_id"],
            executor_id=new_order["executor_id"]
        )
        db.session.add(order_data)
        db.session.commit()
        return f"New order is added to database", 201


@app.route("/orders/<id>", methods=["GET", "PUT", "DELETE"])
def order_by_id(id):
    if request.method == "GET":
        return jsonify(Order.query.get(id).to_dict()), 200
    elif request.method == "PUT":
        new_order = json.loads(request.data)
        order = Order.query.get(id)
        order.name = new_order["name"]
        order.description = new_order["description"]
        order.start_date = new_order["start_date"]
        order.end_date = new_order["end_date"]
        order.address = new_order["address"]
        order.price = new_order["price"]
        order.customer_id = new_order["customer_id"]
        order.executor_id = new_order["executor_id"]

        db.session.add(order)
        db.session.commit()
        return f"Order {id} is updated", 204

    elif request.method == "DELETE":
        order = Order.query.get(id)
        db.session.delete(order)
        db.session.commit()
        return f"Order {id} is deleted", 204


@app.route("/offers", methods=["GET", "POST"])
def all_offers():
    if request.method == "GET":
        result = []
        for offer in Offer.query.all():
            result.append(offer.to_dict())
        return jsonify(result), 200

    elif request.method == "POST":
        new_offer = json.loads(request.data)
        offer_data = Offer(
            id=new_offer["id"],
            order_id=new_offer["order_id"],
            executor_id=new_offer["executor_id"]
        )

        db.session.add(offer_data)
        db.session.commit()
        return f"New offer is added to database", 201


@app.route("/offers/<id>", methods=["GET", "PUT", "DELETE"])
def offer_by_id(id):
    if request.method == "GET":
        return jsonify(Offer.query.get(id).to_dict()), 200
    elif request.method == "PUT":
        new_offer = json.loads(request.data)
        offer = Offer.query.get(id)
        offer.order_id = new_offer["order_id"]
        offer.executor_id = new_offer["executor_id"]

        db.session.add(offer)
        db.session.commit()
        return f"Order {id} is updated", 204

    elif request.method == "DELETE":
        offer = Offer.query.get(id)
        db.session.delete(offer)
        db.session.commit()
        return f"Offer {id} is deleted", 204


app.run(debug=True)
