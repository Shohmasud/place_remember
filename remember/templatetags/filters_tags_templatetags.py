from django import template
from remember.models import UserLogFB,RememberPlaceFB,RememberPlaceVk,UserLogVk
from django.contrib.auth.models import User
import re
register = template.Library()

users_modelAll = [UserLogFB,UserLogVk]
remembers_modelsAll = [RememberPlaceVk,RememberPlaceFB]
#
@register.filter
def verify_user(value):
    global first_name
    first_name = value
    for elements in users_modelAll:
        try:
            fullname = elements.objects.get(user=value)
            list_releted = [res for data in elements.objects.all() if data.user == value for res in data.releted_place]
            len_change_list = len(list(set(list_releted)))

            if len_change_list == 0:
                return "You don't have any memories"
            return "Add more memories"

        except:
            provider = None
            for obj in User.objects.all():
                if obj.first_name == value:
                    provider = obj.username
            matches = re.findall('id[1-9]*', provider)

            if len(matches) == 0:
                try:
                    create_user = UserLogFB.objects.create(user=value)
                    create_user.save()
                    return "You don't have any memories"
                except:
                    return "You don't have any memories"

            try:
                create_user = UserLogVk.objects.create(user=value)
                create_user.save()
                return "You don't have any memories"
            except:
                return "You don't have any memories"

#
@register.simple_tag
def place():
    dict_user_name = dict()

    for objects in users_modelAll:
        for data in objects.objects.all():
            if data.user == first_name:
                for tuple_obj in data.releted_place.values_list():
                    dict_user_name[tuple_obj[1]] = [tuple_obj[2]]

    return dict_user_name


#
@register.simple_tag
def tag_pk():
    return first_name
