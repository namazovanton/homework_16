import json


def open_users():
    """Открывает файл Users.json. Возвращает данные в виде списка."""
    with open('data/Users.json', 'rt', encoding='utf-8') as file:
        users_list = json.load(file)
        return users_list


def open_orders():
    """Открывает файл Orders.json. Возвращает данные в виде списка."""
    with open('data/Orders.json', 'rt', encoding='utf-8') as file:
        orders_list = json.load(file)
        return orders_list


def open_offers():
    """Открывает файл Offers.json. Возвращает данные в виде списка."""
    with open('data/Offers.json', 'rt', encoding='utf-8') as file:
        offers_list = json.load(file)
        return offers_list
# def search_user_by_id(id):
#     """Открывает файл Users.json. Ищет пользователя по id.
#     Возвращает данные в виде экземпляра класса User."""
#     users_list = open_users()
#     for user in users_list:
#         if user["id"] == id:
#             new_user = main.User(
#                 id=user["id"],
#                 first_name=user["first_name"],
#                 last_name=user["last_name"],
#                 age=user["age"],
#                 email=user["email"],
#                 role=user["role"],
#                 phone=user["phone"]
#             )
#         else:
#             continue
#         return new_user


# def search_order_by_id(id):
#     """Открывает файл Orders.json. Ищет заказ по id.
#     Возвращает данные в виде экземпляра класса Order."""
#     orders_list = open_orders()
#     for order in orders_list:
#         if order["id"] == id:
#             new_order = main.Order(
#                 id=order["id"],
#                 name=order["name"],
#                 description=order["description"],
#                 start_date=order["start_date"],
#                 end_date=order["end_date"],
#                 address=order["address"],
#                 price=order["price"],
#                 customer_id=order["customer_id"],
#                 executor_id=order["executor_id"]
#             )
#         else:
#             continue
#         return new_order


# def search_offer_by_id(id):
#     """Открывает файл Offers.json. Ищет заказ по id.
#     Возвращает данные в виде экземпляра класса Offer."""
#     offers_list = open_offers()
#     for offer in offers_list:
#         if offer["id"] == id:
#             new_offer = main.Offer(
#                 id=offer["id"],
#                 order_id=offer["order_id"],
#                 executor_id=offer["executor_id"]
#             )
#         else:
#             continue
#         return new_offer