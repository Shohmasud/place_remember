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

class TestFormPostView(TestCase):
    def client(self):
        self.client = Client()

    def test_form_is_valib(self):
        self.data = {'address':'Krasnoyarsk','comment':'Nice'}
        self.form = RememberForm(data=self.data)
        self.assertEqual(False,self.form.is_valid())

    def test_providef_fb(self):
        self.create_userFacebook = UserLogFB.objects.create(user='Nams')
        self.create_User = User.objects.create(first_name='Nams')
        self.create_User_provider = User.objects.create(username='nams')
        self.assertEqual(0,len(re.findall('id[1-9]*',self.create_User_provider.username)))

    def test_providef_vk(self):
        self.create_userVk = UserLogVk.objects.create(user='Nam')
        self.create_User = User.objects.create(first_name='Nam')
        self.create_User_provider = User.objects.create(username='id45564645')
        self.assertEqual('id45564645', re.findall('id[1-9]*', self.create_User_provider.username)[0])

    def test_remember_place(self):
        self.data = {'address': 'Krasnoyarsk', 'comment': 'Nice'}
        self.create_userVk = UserLogVk.objects.create(user='Nam')
        self.create_userFacebook = UserLogFB.objects.create(user='Nams')
        self.create_RememberFacebook = RememberPlaceFB.objects.create(place=self.data['address'],comment=self.data['comment'])
        self.assertEqual('Nam', self.create_userVk.user)
    #
    def test_get_placeRemember(self):
        self.data = {'address': 'Krasnoyarsk', 'comment': 'Nice'}

        self.create_userFacebook = UserLogFB.objects.create(user='Namsmqweasx')
        self.create_userVk = UserLogVk.objects.create(user='Namqewmin')

        self.create_RememberFacebook = RememberPlaceFB.objects.create(place=self.data['address'],comment=self.data['comment'])
        self.reletedFacebook = self.create_userFacebook.releted_place.add(self.create_RememberFacebook)
        self.create_RememberVK = RememberPlaceVk.objects.create(place=self.data['address'],comment=self.data['comment'])
        self.reletedVK = self.create_userVk.releted_place.add(self.create_RememberVK)

        if self.create_userFacebook.user == UserLogFB.objects.create(user='Namsmswqeaax').user:
            self.resultFB = self.create_userFacebook.releted_place.values_list()[0]
            self.assertEqual(tuple, type(self.resultFB))

        self.resultVK = self.create_userVk.releted_place.values_list()[0]
        self.assertEqual(tuple, type(self.resultVK))

    def test_post(self):
        response = self.client.post('/sign/social/',{'form':RememberForm()})
        print(response.status_code)
        self.assertEqual(200,response.status_code)
