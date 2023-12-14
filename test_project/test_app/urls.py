from django.urls import path
from . import views


urlpatterns=[
    path('home/',views.home,name='home'),
    path('blog/',views.blog,name="blog"),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('product/',views.product,name='product'),
    path('',views.order,name='order'),
    path('customers/<str:pk_test>/',views.customers,name='customers'),
    path('order_form/',views.order_form,name='order_form')
]