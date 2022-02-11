from django.urls import path
from . import views

# empty string is the root of the app
urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
]