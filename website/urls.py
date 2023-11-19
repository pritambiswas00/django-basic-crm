from django.urls import path
from .views import home, logout_user, register_user, record_user,delete_record,add_record, update_record


# Setting route for the Website
urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('record/<int:id>', record_user, name='record'),
    path('delete_record/<int:id>', delete_record, name='delete_record'),
    path('add_record/', add_record, name='add_record'),
    path('update_record/<int:id>', update_record, name='update_record'),
]