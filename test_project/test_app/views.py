from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from .filter import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    
    return render(request,'test_app/home.html')

@login_required(login_url='login')
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


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            print(username)
       
            password=request.POST.get('password')
            print(password)
            user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"username or password is invalid")

        return render(request,'test_app/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=CreateUserForm()
    
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            print(request.POST.get('email'))
            if form.is_valid():
                print("ok")
                user=form.cleaned_data.get('username')
            
                messages.success(request,'Account created sucessfully for' + user)
                form.save()
                return redirect('login')
            else:
                print('error')

        context={'form':form}
        return render(request,'test_app/register.html',context)

@login_required(login_url='login')
def product(request):
    products = Product.objects.all()

    return render(request,'test_app/product.html',{'products':products})

@login_required(login_url='login')
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


@login_required(login_url='login')
def customers(request,pk_test):
    cust=customer.objects.get(id=pk_test)
    orders=cust.order_set.all()
    order_count=orders.count()
    context1={'customer':cust,'orders':orders,'order_count':order_count}
    return render(request,'test_app/customers.html',context1)

@login_required(login_url='login')
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

@login_required(login_url='login')
def UpdateOrder(request, pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method == 'POST':
        #print('Printing POST:',request.POST)
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'test_app/order_form.html',context)

@login_required(login_url='login')
def delete(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request,'test_app/delete.html',context)

def logout_page(request):
    logout(request)
    return redirect('home')

    