from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('blog/',views.blog,name="blog"),
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('product/',views.product,name='product'),
    path('order/',views.order,name='order')
]