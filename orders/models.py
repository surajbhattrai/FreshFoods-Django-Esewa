from django.db import models
from app.models import Account
from store.models import Product

class Order(models.Model):
    STATUS ={
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    }        

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=100, default="", null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    address_line_1 = models.CharField(max_length=100, blank=True)
    address_line_2 = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_note = models.CharField(max_length=100,blank=True)
    order_total = models.CharField(max_length=30, default="", null=True)
    status = models.CharField(max_length=10, choices=STATUS, default="New")
    ip = models.CharField(blank=True ,max_length=10,  default="", null=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
     
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'

    def __str__(self):
        return self.first_name
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name
    
    