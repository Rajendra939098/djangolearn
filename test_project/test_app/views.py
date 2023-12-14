from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# Create your views here.
def home(request):
    
    return render(request,'test_app/home.html')

def blog(request):
    orders=Order.objects.all()
    customers=customer.objects.all()
    
    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='pending').count()


    context={'orders':orders,'customers':customers,'total_orders':total_orders,
             'delivered':delivered,'pending':pending,'total_customers':total_customers }


    return render(request,"test_app/blog.html",context)

def login(request):
    return render(request,'test_app/login.html')


def register(request):
    return render(request,'test_app/register.html')

def product(request):
    products = Product.objects.all()

    return render(request,'test_app/product.html',{'products':products})
def order(request):

    orders=Order.objects.all()
    customers=customer.objects.all()
    
    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='pending').count()

    context={'orders':orders,'customers':customers,'total_orders':total_orders,
             'delivered':delivered,'pending':pending,'total_customers':total_customers }
    return render(request,'test_app/order.html',context)



def customers(request,pk_test):
    cust=customer.objects.get(id=pk_test)
    orders=cust.order_set.all()
    order_count=orders.count()
    context1={'customer':cust,'orders':orders,'order_count':order_count}
    return render(request,'test_app/customers.html',context1)

def order_form(request):
    form=OrderForm()
    if request.method == 'POST':
        #print('Printing POST:',request.POST)
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}

    return render(request,'test_app/order_form.html',context)