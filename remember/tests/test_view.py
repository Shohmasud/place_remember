from remember.models import UserLogFB,UserLogVk,RememberPlaceVk,RememberPlaceFB
from django.test import TestCase
from remember.forms import RememberForm
from django.contrib.auth.models import User
import re

from django.test import Client
csrf_client = Client(enforce_csrf_checks=True)

