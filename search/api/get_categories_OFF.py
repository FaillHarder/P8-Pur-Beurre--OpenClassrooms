import requests


def get_categories(number):

    liste_of_categories = list()

    url = 'https://fr.openfoodfacts.org/categories.json'

    while len(liste_of_categories) != number:

        response = requests.get(url)
        response_json = response.json()

        for cat in response_json["tags"]:
            category = cat.get("name")
            liste_of_categories.append(category)

            if len(liste_of_categories) == number:
                return liste_of_categories

list_cate = get_categories(400)
print(list_cate)
print(len(list_cate))