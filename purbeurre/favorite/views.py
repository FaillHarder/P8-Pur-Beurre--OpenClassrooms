from django.core.paginator import Paginator
from favorite.models import Favorite
from search.models import Product
from django.shortcuts import render


# Create your views here.

def product_save(request):
    
    # if request.method == "GET":
    user = request.user
    substitue = request.GET.get("substitute")
    substitue_save = Product.objects.get(bar_code=substitue)
    Favorite().save_substitute(user, substitue_save)

    return render(request, "product_save.html")



def myfood(request):

    my_fav = Favorite.objects.filter(user=request.user)
    my_fav_products = [fav.product_favorite for fav in my_fav]
    paginator = Paginator(my_fav_products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "favorites": page_obj
    }

    return render(request, "myfood.html", context)

def description(request):

    product = request.GET.get("query")
    product_description = Product.objects.get(bar_code=product)
    context = {
        "product": product_description
    }
    return render(request, "description.html", context)