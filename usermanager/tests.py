from usermanager.views import registrer

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="test", password="test")
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
        view = registrer(request)
        self.assertEqual(view.status_code, 302)

        user = User.objects.all()
        self.assertEqual(len(user), 2)


        
        
        