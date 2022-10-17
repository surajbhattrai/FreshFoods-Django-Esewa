from django.contrib import admin
import admin_thumbnails
from .models import Product , ReviewRating, ProductGalary
# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProductGalaryInline(admin.TabularInline):
    model = ProductGalary
    extra =1

@admin_thumbnails.thumbnail('image')
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','price','category','created_date','is_available']
    prepopulated_fields = {'slug':('product_name',)}
    ordering = ['-created_date']
    inlines = [ProductGalaryInline]


admin.site.register(ReviewRating)
admin.site.register(ProductGalary)
admin.site.register(Product,ProductAdmin)
