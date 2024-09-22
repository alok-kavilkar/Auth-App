from django.urls import path, include
from .views import index, create_user
urlpatterns = [
    path('', index, name='index'),
    path('create-user/', create_user, name='create-user')
]