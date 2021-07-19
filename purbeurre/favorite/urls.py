from favorite import views
from django.urls import path

urlpatterns = [
    path('myfood', views.myfood, name='myfood'),
]