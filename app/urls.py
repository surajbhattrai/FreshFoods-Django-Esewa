from django.urls import path
from .import views
from .views import   ProductDetailView

urlpatterns = [
     path('', views.home, name='home'),
     path('product/<int:pk>/',ProductDetailView.as_view(),name='product-detail')
]
