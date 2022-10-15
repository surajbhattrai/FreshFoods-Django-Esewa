from django.urls import path
from .import views

urlpatterns = [
    path('place_order/',views.place_order,  name='place-order'),
    path('payments/', views.payments,name='payments'),
    path('order_complete/', views.order_complete,name='order_complete'),

    path('esewarequest/',views.EsewaRequestView.as_view(),name='esewarequest'),
    path('esewa-verify/',views.EsewaVerifyView.as_view(),name='esewaverify'),
]
