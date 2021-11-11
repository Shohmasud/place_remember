from remember.models import UserLogFB,RememberPlaceFB,RememberPlaceVk,UserLogVk
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import render
from remember.forms import RememberForm
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
    """"""