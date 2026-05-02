# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render

# def favorite_list(request):
#     return render(request, 'favorites/favorite_list.html')
from django.shortcuts import render, redirect
from .models import Favorite
from django.contrib.auth.decorators import login_required
from movies.views import OMDB_API_KEY
import requests
from django.conf import settings

api_key = settings.OMDB_API_KEY


@login_required
def add_favorite(request, imdb_id):
    url = f"http://www.omdbapi.com/?apikey={'32bf578e'}&i={imdb_id}"
    response = requests.get(url)
    data = response.json()
    if data.get('Title'):
        Favorite.objects.get_or_create(
            user=request.user,
            imdb_id=imdb_id,
            title=data['Title'],
            poster=data.get('Poster', ''),
            year=data.get('Year', '')
        )
    return redirect('favorite_list')

@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites/favorite_list.html', {'favorites': favorites})
