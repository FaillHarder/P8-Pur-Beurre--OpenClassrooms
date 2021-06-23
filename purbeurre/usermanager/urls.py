from usermanager import views
from django.urls import path

urlpatterns = [
    path('registrer', views.registrer, name='registrer'),
    path('login', views.login, name='login'),
]