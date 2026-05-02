from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite_list, name='favorite_list'),
    path('add/<str:imdb_id>/', views.add_favorite, name='add_favorite'),

]
