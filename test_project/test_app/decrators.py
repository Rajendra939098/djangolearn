from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decrators(view_func):
        def wrapper_func(request,*arg,**kwargs):

            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*arg,**kwargs)
            else:
                return HttpResponse('Your are not authorised to view this page')
        return wrapper_func
    return decrators

def admin_only(view_func):
    def wrapper_function(request,*arg,**kwargs):
        group=None
        
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group == None:
            return HttpResponse("error")
        
        if group == 'customer':
            return redirect('blog')
        
        if group == 'admin':
            return view_func(request,*arg,**kwargs)
    return wrapper_function
