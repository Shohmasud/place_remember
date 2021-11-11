from remember.models import UserLogFB,UserLogVk,RememberPlaceVk,RememberPlaceFB
from django.test import TestCase
from remember.forms import RememberForm
from django.contrib.auth.models import User
import re

from django.test import Client
csrf_client = Client(enforce_csrf_checks=True)

class TestLoginView(TestCase):
    def client(self):
        self.client = Client()
    def test_get(self):
        response = self.client.get('/login/')
        print(response.status_code)
        self.assertEqual(200,response.status_code)


class TestSignView(TestCase):
    def client(self):
        self.client = Client()

    def test_get(self):
        response = self.client.post('/sign/social/',{'form':RememberForm()})
        print(response.status_code)
        self.assertEqual(200,response.status_code)

