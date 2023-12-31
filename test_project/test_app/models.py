from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    date_created =models.DateTimeField(auto_now_add=True,null=True)
    profile_pic=models.ImageField(default="profile.jpeg", null=True,blank=True)

    #def __str__(self):
    #    print(self.user.username)
       # return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY=(
        ('indore','indore'),
        ('outdore','outdore')
    )
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    description=models.CharField(max_length=200,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('Delivered','Delivered')
    )
    customer=models.ForeignKey(customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.product.name
    
