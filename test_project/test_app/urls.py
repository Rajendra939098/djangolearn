from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('blog/',views.blog,name="blog"),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register')
]