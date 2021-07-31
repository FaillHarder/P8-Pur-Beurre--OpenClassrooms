from search.models import Product, Category

from django.core.management.base import BaseCommand
from django.db import IntegrityError
import json
import requests


class Command(BaseCommand):
    help = 'Ajout des catégories et produits dans la bdd'
    
    def handle(self, *args, **options):

        params = self.read_json_file("search/management/settings.json")
        for category in params["categories"]:
            Category.objects.update_or_create(name=category)
            response_json = self.request_api_OFF(category, params["fields"], params["page"])
            for product_data in response_json["products"]:
                try:
                    # ignore les produits sans nom
                    if len(product_data["product_name_fr"]) > 1:
                        data = {
                            "product_name": product_data["product_name_fr"],
                            "bar_code": product_data["id"],
                            "nutriscore": product_data["nutriscore_grade"],
                            "proteins_100g": product_data["proteins_100g"],
                            "energy_100g": product_data["energy_100g"],
                            "fat_100g": product_data["fat_100g"],
                            "fiber_100g": product_data["fiber_100g"],
                            "carbohydrates_100g": product_data["carbohydrates_100g"],
                            "salt_100g": product_data["salt_100g"],
                            "saturated_fat_100g": product_data["saturated-fat_100g"],
                            "sugars_100g": product_data["sugars_100g"],
                            "image": product_data["image_front_url"],
                            "url": product_data["url"],
                        }
                    else:
                        continue
                except KeyError:
                    continue

                try:
                    data_product = Product(data["product_name"], *list(data.values())[1:])
                    data_product.save()
                    cate = Category.objects.get(name=category)
                    Product.objects.get(bar_code=data["bar_code"]).categories.add(cate)
                except IntegrityError:
                    continue
                # ajoute la relation manytomany entre produit et category
                

        self.write_json_file_next_page("search/management/settings.json", params)


    def read_json_file(self, json_file):
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def write_json_file_next_page(self, json_file, json_file_r):
        json_file_r["page"] +=1
        with open(json_file, "w", encoding="utf-8") as outfile:
            json.dump(json_file_r, outfile, indent=4, ensure_ascii=False)

    def request_api_OFF(self, category, fields, page):
        response = requests.get(
            url="https://fr.openfoodfacts.org/cgi/search.pl",
            params={
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": category,
                "tag_1": "A",
                "json": "true",
                "fields": ",".join(fields),
                "page_size": 100,
                "page": page
            }
        )
        response_json = response.json()
        return response_json