# # # from django.shortcuts import render

# # # # Create your views here.
# # # import requests
# # # from django.shortcuts import render

# # # OMDB_API_KEY = "32bf578e"  # paste your key here

# # # def search_movies(request):
# # #     query = request.GET.get("query")
# # #     movies = []
# # #     if query:
# # #         url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={query}"
# # #         response = requests.get(url)
# # #         if response.status_code == 200:
# # #             data = response.json()
# # #             if data.get("Search"):
# # #                 movies = data["Search"]
# # #     return render(request, "movies/movie_list.html", {"movies": movies})

# # # def movie_detail(request, imdb_id):
# # #     url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i={imdb_id}&plot=full"
# # #     response = requests.get(url)
# # #     movie = response.json() if response.status_code == 200 else None
# # #     return render(request, "movies/movie_detail.html", {"movie": movie})

# # from django.shortcuts import render
# # import requests

# # # Movie list view
# # def movie_list(request):
# #     query = request.GET.get('query', '')  # search query
# #     movies = []

# #     if query:
# #         url = f"http://www.omdbapi.com/?apikey=32bf578e&s={query}&type=movie"
# #         response = requests.get(url)
# #         data = response.json()
# #         movies = data.get('Search', [])

# #     return render(request, "movies/movie_list.html", {"movies": movies, "query": query})

# # # Movie detail view
# # def movie_detail(request, imdb_id):
# #     url = f"http://www.omdbapi.com/?apikey=32bf578e&i={imdb_id}"
# #     response = requests.get(url)
# #     movie = response.json()
# #     return render(request, "movies/movie_detail.html", {"movie": movie})


# # movies/views.py
# from django.shortcuts import render
# from django.conf import settings
# import requests

# OMDB_API_KEY = "32bf578e"  # your API key

# # Then in your movie_detail
# def movie_detail(request, imdb_id):
#     url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i={imdb_id}"
#     response = requests.get(url)
#     movie = response.json()
#     return render(request, "movies/movie_detail.html", {"movie": movie})

# def movie_list(request):
#     # query = request.GET.get('query', '')
#     movies = []
#     if query:
#         url = f"http://www.omdbapi.com/?apikey={settings.OMDB_API_KEY}&s={query}"
#         response = requests.get(url)
#         data = response.json()
#         movies = data.get('Search', [])
#     return render(request, "movies/movie_list.html", {"movies": movies})



from django.shortcuts import render
from django.conf import settings
import requests
OMDB_API_KEY = "32bf578e"  # your API key

def movie_list(request):
    query = request.GET.get('query', '')
    movies = []
    if query:
        url = f"http://www.omdbapi.com/?apikey={settings.OMDB_API_KEY}&s={query}"
        response = requests.get(url)
        data = response.json()
        movies = data.get('Search', [])
    return render(request, "movies/movie_list.html", {"movies": movies})

def movie_detail(request, imdb_id):
    url = f"http://www.omdbapi.com/?apikey={settings.OMDB_API_KEY}&i={imdb_id}"
    response = requests.get(url)
    movie = response.json()
    return render(request, "movies/movie_detail.html", {"movie": movie})
