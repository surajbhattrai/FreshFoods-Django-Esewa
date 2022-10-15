from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=300, blank=True)
    cart_image = models.ImageField(upload_to='categories/photos', blank=True)

    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])    


    class Meta:
        verbose_name = 'catgory'
        verbose_name_plural = 'categories'    
    

