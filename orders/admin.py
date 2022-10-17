from django.contrib import admin
from .models import Order, OrderProduct
# Register your models here.

class OrderProductLine(admin.TabularInline):
    model  = OrderProduct
    extra = 0
    readonly_fields = ['user', 'product', 'quantity', 'product_price', 'ordered']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone_number', 'email', 'city', 'order_total','status', 'is_ordered','created_at']
    list_filter = ['is_ordered']
    search_fields = ['order_number','first_name', 'last_name', 'phone_number', 'email']
    list_per_page = 2
    inlines  = [OrderProductLine]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
