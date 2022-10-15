from django.shortcuts import render
from store.models import Product, ReviewRating, ProductGalary
from django.views.generic import  DetailView
from orders.models import OrderProduct


# Create your views here.

def home(request):
    products = Product.objects.all().filter(is_available=True)
    for product in products:
        
        reviews  = ReviewRating.objects.filter(product_id=product.id, status=True)
          

    context = {
        'products' : products,
        'reviews': reviews,
    }
    return render(request, 'home.html',context)



class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self,product_id=None, **kwargs):
        context = super(ProductDetailView,self).get_context_data(**kwargs)
        context['reviews'] = ReviewRating.objects.filter(product_id=self.object.id, status=True)
        context['product_galary'] = ProductGalary.objects.filter(product_id=self.object.id)
        context['all_products'] = Product.objects.all()[0:6]

        if self.request.user.is_authenticated:
            try:
              context['orderproduct'] = OrderProduct.objects.filter(user=self.request.user, product_id=self.object.id).exists()
            except OrderProduct.DoesNotExist:
               orderproduct = None
        else:
            orderproduct= None       
            
               
        return context
    
        
   
    
