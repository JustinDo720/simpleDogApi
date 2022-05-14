from django.urls import path
from . import views

urlpatterns = [
    path('add_dog/', views.DogAPI.as_view()),
]
