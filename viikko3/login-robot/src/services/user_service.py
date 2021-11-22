from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
            
        if len(username) < 3:
            raise UserInputError("Username is too short")
            
        if len(password) < 8:
            raise UserInputError("Password is too short")
            
        numbers = ["1","2","3","4","5","6","7","8","9","0"]
        tru = 0
        for letter in password:
            if letter in numbers:
                tru = 1
        if tru == 0:
            raise UserInputError("Password only has letters")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
