from django.contrib import admin
from django.urls import path, include


# //Setting route for the Main App//
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls'))
]
