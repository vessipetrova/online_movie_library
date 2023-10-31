class Admin:
    def __init__(self, admin_id, name, pin, admin_email, user_email):
        self.admin_id = admin_id
        self.name = name
        self.pin = pin
        self.__admin_email = set()
        self.__user_email = set()

    def __str__(self):
        return f"Admin ID: {self.admin_id}\n" \
               f"Name: {self.name}\n" \
               f"Pin: {self.pin}\n"

    def add_movie_to_library(self, library, movie):
        library.add_movie(movie)

    def remove_movie_from_library(self, library, movie, remove_all=False):
        library.remove_movie(movie, remove_all)

    def get_user_email(self, user):
        self.__user_email.add(user)
        return self.__user_email

    def set_user_email(self, new_email):
        self.__user_email: "" = new_email
        return self.__user_email

    def get_admin_id(self):
        return self.admin_id

    def set_admin_id(self, new_id):
        self.admin_id = new_id
        return self.admin_id

    def get_name(self):
        return self.name

    def get_pin(self):
        return self.pin

    def __hash__(self):
        return hash(self.admin_id) + hash(self.name) + hash(self.pin) + hash(self.__user_email)

    def check_user_id(self, user, user_id):
        return user_id == user.get_user_id()

    def check_user_name(self, user, name):
        return name == user.get_name()

    def check_user_email(self, user, email):
        return email == user.get_user_email()

