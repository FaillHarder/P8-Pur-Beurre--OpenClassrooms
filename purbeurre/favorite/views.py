from django.shortcuts import render

# Create your views here.
def myfood(request):

    return render(request, 'myfood.html')
