from django.contrib import admin
from django.urls import path,include
from remember.views import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^accounts/',include('allauth.urls')),
    path('login/', LoginView.as_view()),
]
