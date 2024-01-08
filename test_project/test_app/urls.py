from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('blog/',views.blog,name="blog"),
    path('login/',views.login_page,name='login'),
    path('register/',views.register,name='register'),
    path('product/',views.product,name='product'),
    path('order/',views.order,name='order'),
    path('customers/<str:pk_test>/',views.customers,name='customers'),
    path('order_form/',views.order_form,name='order_form'),
   
    path('update_order/<str:pk>/',views.UpdateOrder,name='update_order'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('logout/',views.logout_page,name='logout'),
    path('userpage/',views.userpage,name='userpage'),
    path('settings/',views.settings_page,name='settings')
]