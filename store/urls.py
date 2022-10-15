from django.urls import path
from .import views

urlpatterns = [
    path('',views.store, name='store'),
    path('<slug:category_slug>/',views.store, name='products_by_category'),
    path('submit_review/<int:product_id>/',views.submit_reviews,name='submit_reviews'),
]
