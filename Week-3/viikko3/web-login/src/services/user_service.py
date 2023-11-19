from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password, password_confirmation)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password or not password_confirmation:
            raise UserInputError("Username ,password and password_confirmation are required")
        elif len(username) < 3:
            print('Testing')
            raise UserInputError("Username needs to be at least 3 characters long")
        elif not re.match('^[a-z]+$', username):
            raise UserInputError("Username should consist of lowercase letters only")
        elif not re.search(r'[!@#$%^&*()-_=+{};:,<.>?]', password) or len(password) < 8:
            raise UserInputError("Password must contain at least one special character and be at least 8 characters long")
        elif password_confirmation != password:
            raise UserInputError("Password Confirmation does not match the given password")
        
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


user_service = UserService()
