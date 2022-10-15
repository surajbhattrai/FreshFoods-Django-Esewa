from django.contrib import admin
from .models import Cart, CartItem





# Register your models here.


class CartAdminManager(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']
    ordering = ('-date_added',)

class CartItemManager(admin.ModelAdmin):
    list_display = ['product','cart','quantity','is_active']
    list_display_links = ('product', 'cart', 'quantity', 'is_active',)
    ordering = ('-date_created',)    

admin.site.register(Cart, CartAdminManager)
admin.site.register(CartItem, CartItemManager)