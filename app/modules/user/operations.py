from flask_bcrypt import generate_password_hash

from app.database import User, Users


def create(name: str, password: str) -> None:
    password_hash = generate_password_hash(password, 10)
    user = User(name, password_hash)
    User.save(user)


def get_all() -> Users:
    return User.find_all()


def get_one_by_id(id: int) -> User:
    return User.find_first_or_404_by_id(id)
