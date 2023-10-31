from Movies import Movie
from MovieLibrary import MovieLibrary
from Users import User
from Admins import Admin
from Subscriptions import Subscription

movie1 = Movie(title="Star Wars",
               director="Stephen Spielberg",
               genre="Sci-Fi",
               release_date="01/04/1989",
               movie_id=1)

movie2 = Movie(title="Star Wars",
               director="Stephen Spielberg",
               genre="Sci-Fi",
               release_date="1/4/1989",
               movie_id=2)

movie3 = Movie(title="Star Wars 3",
               director="Stephen Spielberg",
               genre="Sci-Fi",
               release_date="15/5/2001",
               movie_id=3)

movie4 = Movie(title="Star Wars 3",
               director="Stephen Spielberg",
               genre="Sci-Fi",
               release_date="15/5/2001",
               movie_id=4)

print("Movie 1: ", movie1)
print("Movie 2: ", movie2)
print("Movie 3: ", movie3)

user1 = User(user_id=1,
             name="Viktor",
             pin="9999999999",
             user_email="zarrie@gmail.com",
             rented_movies="movie1",
             favourite_movies="movie2",
             watched_movies="movie2",
             subscription_id="Gold",
             subscription_type=Subscription("Gold", 3, 3),
             password=123457)

user2 = User(user_id=2,
             name="Mitko",
             pin="9999999997",
             user_email="mitko@gmail.com",
             rented_movies="movie2",
             favourite_movies="movie1",
             watched_movies="",
             subscription_id="Silver",
             subscription_type=Subscription("Silver", 2, 2),
             password=123456)

user3 = User(user_id=3,
             name="Gosho",
             pin="9999999995",
             user_email="gosho@gmail.com",
             rented_movies="movie4",
             favourite_movies="movie3",
             watched_movies="movie3",
             subscription_id="Crystal",
             subscription_type=Subscription("Crystal", 1, 1, ),
             password=123458)

print("User 1: ", user1)
print("User 2: ", user2)
print("User 3: ", user3)

library1 = MovieLibrary(library_id=1,
                        web_address="MovieCloud2",
                        movies_list=[movie1, movie2, movie3],
                        rented_movies=[movie1, movie2, movie3],
                        users=[user1])

print("Library 1: ", library1)

print("Users in library 1 before adding: ", library1.get_users())

library1.add_user(user2)
library1.add_user(user3)

print("Users in library 1 after adding: ", library1.get_users())

print("Available movies in library 1: ", library1.get_available_movies())

print("Rented movies of User 1: ", user1.get_rented_movies())

print("This should be a error -> ", library1.rent_movie(movie1, user1))


library1.return_movie(movie=movie2,
                      user=user1)

print("Available movies in library 1: ", library1.get_available_movies())
print("Rented movies of User 1: ", user1.get_rented_movies())

admin1 = Admin(admin_id=1,
               name="Viktor",
               pin="9999999999",
               user_email="zarrie@gmail.com",
               admin_email="zarrie2@gmail.com")

print("Admin 1: ", admin1)
print("Email of User 2: ", admin1.get_user_email(user2))
print("ID of Admin 1:", admin1.get_admin_id())
admin1.set_admin_id(4)
print("ID of Admin 1 after set:", admin1.get_admin_id())
print("Name of Admin 1:", admin1.get_name())
print("Pin of Admin 1:", admin1.get_pin())

print("ID of User 1 is 4: ", admin1.check_user_id(user1, 4))
print("Name of User 1 is Viktor: ", admin1.check_user_name(user1, "Viktor"))

library1.add_movie(movie2)
print("Available movies in library 1: ", library1.get_available_movies())
admin1.add_movie_to_library(library1, movie4)
print("Available movies in library 1 after add: ", library1.get_available_movies())
admin1.remove_movie_from_library(library1, movie4)
print("Available movies in library 1 after remove: ", library1.get_available_movies())

print("Ratings of Movie 1: ", movie1.get_ratings())
print("Rate movie 1 as User 1: ", user1.rate_movie(movie1, 5))
print("Ratings of Movie 1: ", movie1.get_ratings())