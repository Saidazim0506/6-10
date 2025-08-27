from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie
from .forms import MovieForm

def index(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()

    context = {
         "genres": genres,
         "movies": movies,
    }

    return render(request, "movies/index.html", context)

def genre_movies(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    movies = genre.movies.all()

    context = {
        "genre": genre,
        "movies": movies
    }

    return render(request, "movies/index.html", context)

def movie_detail(request, pk: int):
    genres = Genre.objects.all()
    movie = get_object_or_404(Movie, pk=pk)

    context = {
        "genres": genres,
        "movie": movie
    }

    return render(request, "movies/detail.html", context)

def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movies = form.save()
            return redirect("movie_detail", movies.pk)
    else:
        form = MovieForm()

    context = {
        "form": form
    }

    return render(request, "movies/add_movie.html", context)
