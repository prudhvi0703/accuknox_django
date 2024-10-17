from django.contrib import admin
from django.urls import path
from users.views import create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-user/', create_user),
]
