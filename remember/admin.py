from django.contrib import admin
from .models import RememberPlaceFB,UserLogFB,UserLogVk,RememberPlaceVk

# Register your models here.
class Admin_RememberPlaceFB(admin.ModelAdmin):
    list_display = ('id', 'place','comment')
    search_fields = ['id','place','comment']
admin.site.register(RememberPlaceFB,Admin_RememberPlaceFB)

class Admin_RememberPlaceVK(admin.ModelAdmin):
    list_display = ('id', 'place','comment')
    search_fields = ['id','place','comment']
admin.site.register(RememberPlaceVk,Admin_RememberPlaceVK)
