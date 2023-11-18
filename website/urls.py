from django.urls import path
from .views import home, logout_user, register_user


# Setting route for the Website
urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
]