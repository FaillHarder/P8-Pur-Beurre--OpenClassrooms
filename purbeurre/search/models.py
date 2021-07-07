from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Product(models.Model):

    product_name = models.CharField(max_length=200)
    bar_code = models.CharField(max_length=20, primary_key=True)
    nutriscore = models.CharField(max_length=2)
    proteins_100g = models.DecimalField(max_digits=7, decimal_places=2)
    energy_100g = models.DecimalField(max_digits=7, decimal_places=2)
    fat_100g = models.DecimalField(max_digits=7, decimal_places=2)
    fiber_100g = models.DecimalField(max_digits=7, decimal_places=2)
    carbohydrates_100g = models.DecimalField(max_digits=7, decimal_places=2)
    salt_100g = models.DecimalField(max_digits=7, decimal_places=2)
    saturated_fat_100g = models.DecimalField(max_digits=7, decimal_places=2)
    sugars_100g = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.TextField()
    url = models.TextField()
    
    def __str__(self):
        return self.product_name

    def search(self, query):
        product_search = Product.objects.filter(product_name__icontains=query)
        return product_search


        
    # fonction pour afficher des produits avec un meilleur score nutri

    # 
class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)
    product = models.ManyToManyField(Product)




# class Favorite(models.Model):
#     # user et produit FK
#     pass