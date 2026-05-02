# from django.urls import path
# from . import views

# urlpatterns = [
#     # Example URLs — adjust to your actual views
#     path('signup/', views.signup_view, name='signup'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
# ]
from django.urls import path
from . import views
from django.views.generic import RedirectView

# urlpatterns = [
#     path('', RedirectView.as_view(pattern_name='login', permanent=False)),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
# ]
# urls.py
# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),   # make sure login_view exists
    path('logout/', views.logout_view, name='logout'), # make sure logout_view exists
]
