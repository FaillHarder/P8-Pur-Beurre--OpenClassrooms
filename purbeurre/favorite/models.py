from django.db.models.fields import EmailField
from search.models import Product
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_favorite = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_favorite.product_name

    def save_substitute(self, user, substitute):

        favorite = Favorite(user=user, product_favorite=substitute)
        favorite.save()
