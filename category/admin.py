from django.contrib import admin
from .models import Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','icon','slug']
    list_editable = ['icon']
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category,CategoryAdmin) 