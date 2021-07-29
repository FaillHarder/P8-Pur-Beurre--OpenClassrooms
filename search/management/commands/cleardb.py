from search.models import Product, Category

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Supprime les catégories'


    def handle(self, *args, **options):
        # créer les catégories manquante
        # Category.objects.all().delete()
        Product.objects.all().delete()