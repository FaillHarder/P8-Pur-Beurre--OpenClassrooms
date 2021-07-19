from search.models import Product
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_favorite = models.ForeignKey(Product, on_delete=models.CASCADE)
