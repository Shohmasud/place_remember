from remember.models import UserLogFB,RememberPlaceFB,RememberPlaceVk,UserLogVk
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import render
from remember.forms import RememberForm
import re
# Create your views here.


class LoginView(View):
    """The class responsible for the output of the login.html file"""
    def get(self, request):
        return render(request, 'login.html')


class SignView(View):
    """The class responsible for the output of the sign.html file"""
    def get(self, request):
        form = RememberForm()
        return render(request, 'sign.html',{'form':form})

class FormPostView(View):
    """The class is responsible for receiving processing and storing data
     on the necessary models (tables of social networks)"""

    def post(self, request, pk):
    #This block we get the user's data and check whether they belong to any provider
        provider = None
        form = RememberForm(request.POST)
        if form.is_valid():
            for obj in User.objects.all():
                if obj.first_name == pk:
                    provider = obj.username
            matches = re.findall('id[1-9]*', provider)

