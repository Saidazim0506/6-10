from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-movie/", views.add_movie, name="add_movie"),
    path("genre/<int:genre_id>/", views.genre_movies, name="genre_movies"),
    path("movie/<int:movie_id>/", views.movie_detail, name="movie_detail"),
]
