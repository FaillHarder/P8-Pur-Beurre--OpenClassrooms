from usermanager import views
from django.urls import path

urlpatterns = [
    path('registrer', views.registrer, name='registrer'),
    path('accounts/login', views.login, name='login'),
    path('myprofile', views.myprofile, name='myprofile'),
]
