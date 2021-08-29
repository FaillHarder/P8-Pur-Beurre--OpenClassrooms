from usermanager.forms import SignUpForm
from usermanager.models import User
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class Signup(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = SignUpForm


class Login(LoginView):
    template_name = 'login.html'


class Logout(LogoutView):
    next_page = reverse_lazy('index')


class Profile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = Profile.extract_username_from_mail(
            str(self.request.user)
        )
        return context

    @staticmethod
    def extract_username_from_mail(mail: str):
        return mail[:mail.find('@')]
