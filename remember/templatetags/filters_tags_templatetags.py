from django import template
from remember.models import UserLogFB,RememberPlaceFB,RememberPlaceVk,UserLogVk
from django.contrib.auth.models import User
import re
register = template.Library()

users_modelAll = [UserLogFB,UserLogVk]
remembers_modelsAll = [RememberPlaceVk,RememberPlaceFB]
