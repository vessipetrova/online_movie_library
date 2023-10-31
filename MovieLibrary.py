class MovieLibrary:
    def __init__(self, library_id, web_address, movies_list, rented_movies, users):
        self.library_id = library_id
        self.web_address = web_address
        self.movies_list = []
        self.rented_movies = []
        self.users = set()

    def add_movie(self, movie):
        if movie not in self.movies_list:
            self.movies_list.append(movie)

    def remove_movie(self, movie, remove_all=False):
        if not remove_all:
            self.movies_list.remove(movie)
        else:
            new_movies_list = []
            for current_movie in self.movies_list: # Remove repeating occurances of current movie in the list
                if current_movie != movie:
                    new_movies_list.append(current_movie)
            self.movies_list = new_movies_list

    def get_users(self):
        return self.users

    def rent_movie(self, movie, user):
        if movie in self.rented_movies:
            return "Movie already rented."
        if user not in self.users:
            return "User not registered in the MovieLibrary."

        if len(user.get_rented_movies()) >= 3:
            return "User has already rented 3 movies."

        is_available = False

        for current_movie in self.movies_list:
            if current_movie == movie:
                is_available = True
                break

        if is_available:
            self.remove_movie(movie)
            self.rented_movies.append(movie)
            user.rent_movie(movie)
        else:
            return "Movie not available"

    def return_movie(self, movie, user):
        if movie not in self.rented_movies:
            return "Movie not rented."
        self.rented_movies.remove(movie)
        self.movies_list.append(movie)
        if movie in user.get_rented_movies():
            user.return_movie(movie)

    def get_available_movies(self):
        result = []
        for movie in self.movies_list:
            result.append(str(movie))
        return result

    def get_rented_movies(self):
        result = []
        for movie in self.rented_movies:
            result.append(str(movie))
        return result

    def add_user(self, user):
        self.users.add(user)

    def remove_user(self, user):
        self.users.remove(user)

    def __str__(self):
        return self.web_address + " " + str(self.library_id)
