from django.urls import path
from . import views

# empty string is the root of the app
urlpatterns = [
    path('', views.index, name='index'),
]