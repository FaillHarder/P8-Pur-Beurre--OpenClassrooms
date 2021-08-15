from usermanager.forms import SignUpForm

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def registrer(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
    else:
        form = SignUpForm()
    return render(request, 'registrer.html', {'form': form})


def myprofile(request):

    return render(request, 'myprofile.html')
