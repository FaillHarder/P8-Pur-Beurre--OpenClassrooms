from usermanager.forms import UserRegistrationForm

from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
def registrer(request):
    
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
            email=request.POST.get("email"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name")
        )

        return redirect("index")

    context = {"form": UserRegistrationForm()}

    return render(request, 'registrer.html', context)


def login(request):
    pass
