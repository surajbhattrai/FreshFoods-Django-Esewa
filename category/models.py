from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from helper import unique_category_slug_generator
from django.db.models.signals import pre_save

class Category(models.Model):
    category_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])      

    class Meta:
        verbose_name = 'catgory'
        verbose_name_plural = 'categories'    

def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug =  unique_category_slug_generator(instance)
pre_save.connect(category_pre_save_receiver, sender=Category)

   

