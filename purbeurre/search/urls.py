from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('search_product', views.search_product, name='search_product'),
]