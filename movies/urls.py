
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.search_movies, name='search_movies'),
#         path('', views.movie_list, name='list'),

#     path('<str:imdb_id>/', views.movie_detail, name='movie_detail'),
# ]


# from django.urls import path
# from . import views

# app_name = "movies"

# urlpatterns = [
#     path('', views.movie_list, name='list'),
#     path('<str:imdb_id>/', views.movie_detail, name='detail'),
# ]


# movies/urls.py
from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.movie_list, name='list'),
    path('<str:imdb_id>/', views.movie_detail, name='detail'),
]
