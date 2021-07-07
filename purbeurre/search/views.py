from search.models import Product
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, "index.html")


def search_product(request):

    if request.method == 'GET':
        query = request.GET.get("query")
        products = Product().search(query)
        
        context = {
            "products": products
        }

        return render(request, "search_product.html", context)