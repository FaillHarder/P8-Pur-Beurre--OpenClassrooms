from django.core import paginator
from search.models import Product
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

# Create your views here.
def index(request):

    return render(request, "index.html")


def search_product(request):
    
    if request.method == "GET":
        query = request.GET.get("query")
        if query != "":
            products_list = Product().search(query)
            if not products_list:
                return(redirect("index")) #créer une page aucun résultat
            else:
                context = {
                    "products": products_list
                }
            return render(request, "search_product.html", context)
        else:
            return(redirect("index"))
    else:
        return(redirect("index"))


def substitute(request):

    if request.method == "GET":
        bar_code = request.GET.get("query")
        product = Product.objects.get(bar_code=bar_code)
        substitutes = Product().substitute(bar_code)
        context = {
            "product": product,
            "substitutes": substitutes
        }
        return render(request, "substitute.html", context)
