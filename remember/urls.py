from django.contrib import admin
from django.urls import path,include
from remember.views import LoginView,SignView,FormPostView
urlpatterns = [
    #http://localhost:8000/path/
    path('admin/', admin.site.urls),
    path(r'^accounts/',include('allauth.urls')),
    path('login/', LoginView.as_view()),
    path('sign/social/',SignView.as_view(),name='sign'),
    path('post/form/<str:pk>/', FormPostView.as_view(), name='post_form_facebook'),
]
