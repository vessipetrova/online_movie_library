class Movie:
    def __init__(self, title, director, genre, release_date, movie_id):
        self.__movie_id = movie_id
        self.title = title
        self.director = director
        self.genre = genre
        self.release_date = release_date
        self.ratings = {}

    def __eq__(self, other):
        if self.title == other.title and \
                self.director == other.director and \
                self.release_date == other.release_date:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.title}, {self.director}, {self.release_date}"

    def get_movie_id(self):
        return self.__movie_id

    def set_movie_id(self, new_id):
        self.__movie_id = new_id
        return self.__movie_id

    def get_title(self):
        return self.title

    def add_rating(self, rating, user):
        self.ratings[user.get_user_id()] = rating

    def get_ratings(self):
        return self.ratings
