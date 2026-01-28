import random
import string
from faker import Faker


def random_email(domain="example.com", length=8):
    # Generate a random string of given length
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{username}@{domain}"

def random_text(name:str=None,length=10):
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return f'{name}-{text}' if name is not None else text


def random_user_data():
    faker = Faker()
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": f"{faker.user_name()}@example.com",
        "position": faker.job(),
        "password": faker.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    }

def random_phone_number():
    return f"+998{''.join(random.choices(string.digits, k=9))}"