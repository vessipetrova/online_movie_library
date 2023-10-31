import random


class User:
    def __init__(self, name, pin, user_id, user_email,
                 rented_movies, favourite_movies, watched_movies,
                 subscription_id, subscription_type, password):
        self.name = name
        self.pin = pin
        self.__user_id = user_id
        self.__rented_movies = []
        self.__favourite_movies = []
        self.__watched_movies = []
        self.__user_email = set()
        self.__subscription_id = subscription_id
        self.__subscription_type = subscription_type
        self.__password = {}

    def rent_movie(self, movie):
        self.__rented_movies.append(movie)

    def return_movie(self, movie):
        self.__rented_movies.remove(movie)

    def get_rented_movies(self):
        result = []
        for movie in self.__rented_movies:
            result.append(str(movie))
        return result

    def __str__(self):
        return f"User ID: {self.__user_id}\n" \
               f"Name: {self.name}\n" \
               f"Pin: {self.pin}\n" \
               f"Subscription ID: {self.__subscription_id}\n" \
               f"Subscription Type: {self.__subscription_type}\n" \
               f"Rented Movies: {self.__rented_movies}\n" \
                f"User Email: {self.__user_email}\n" \
                f"Password: {self.__password}\n"

    def get_subscription_id(self):
        return self.__subscription_id

    def get_subscription_type(self):
        return self.__subscription_type

    def get_user_id(self):
        return self.__user_id

    def add_movie_to_favourite_movies(self, movie, favourite_movies):
        result = []
        for movie in self.__favourite_movies:
            result.append(str(movie))
        return result

    def remove_movie_from_favourite_movies(self, movie, favourite_movies):
        result = []
        for movie in self.__favourite_movies:
            result.append(str(movie))
        return result

    def favourite_movies(self):
        return self.__favourite_movies

    def get_user_email(self):
        return self.__user_email

    def get_name(self):
        return self.name

    def add_watched_movie(self, movie):
        return self.__watched_movies.append(movie)

    def get_watched_movies(self):
        return self.__watched_movies

    def get_reccomended_movies(self, library):
        return random.sample(library.get_available_movies(), 3)

    def rate_movie(self, movie, rating):
        if 0 < rating < 6:
            movie.add_rating(rating, self)
