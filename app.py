import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def mask_card_number(card_number):
    card_str = str(card_number)
    if len(card_str) < 4:
        raise ValueError("Card number too short to mask.")
    return '*' * (len(card_str) - 4) + card_str[-4:]

def get_user_by_id(user_id, users):
    return next((user for user in users if user['id'] == user_id), None)

def calculate_discount(price, percentage):
    if not (0 <= percentage <= 100):
        raise ValueError("Discount must be between 0 and 100")
    return price - (price * (percentage / 100))
