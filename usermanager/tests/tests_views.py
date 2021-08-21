from django.contrib.sessions.middleware import SessionMiddleware
from usermanager.forms import SignUpForm
from usermanager.views import registrer, myprofile
# from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase


# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.username = "username"
        self.password = "secret"

        self.user = User.objects.create_user(username="username", password="secret")
        return super().setUp()

    def test_registrer(self):
        request = self.factory.get("/registrer")
        view = registrer(request)
        self.assertEqual(view.status_code, 200)

        request = self.factory.post("/registrer")
        request.POST = {
            "first_name": "firstnametest",
            "last_name": "lastnametest",
            "email": "test@email.fr",
            "username": "usernametest",
            "password1": "passwordtest",
            "password2": "passwordtest"
        }

        form = SignUpForm(request.POST)
        self.assertTrue(form.is_valid())
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        view = registrer(request)
        # redirect index
        self.assertEqual(view.status_code, 302)

        user = User.objects.all()
        self.assertEqual(len(user), 2)

    def test_my_profile(self):
        request = self.factory.get("/myprofile")
        view = myprofile(request)
        self.assertEqual(view.status_code, 200)
