from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product, ReviewRating
from category.models import Category
from .forms import ReviewForms
from django.contrib import messages

 
def store(request, category_slug=None):
    categories = None
    products = None
    products_count = None
    query = request.GET.get('q',None)
    category_query = request.GET.get('category',None)
    if category_query:
        try:
            categories = Category.objects.get(category_name=category_query)
            products = Product.objects.filter(category=categories,is_available=True)
            products_count = products.count()
        except:
            pass
    elif query:
        products = Product.objects.filter(product_name__icontains=query)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count  = products.count()

    context = {
        'products': products,
        'products_count' :products_count
    }
    return render(request, 'store/store.html',context)

 

def submit_reviews(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForms(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you, your Review has been updated')
            return redirect(url)


        except ReviewRating.DoesNotExist:
            form = ReviewForms(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you, your Review has been submitted')
                return redirect(url)

