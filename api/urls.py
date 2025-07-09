from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    # Order
    path('orders/', views.OrderListCreate.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    # OrderSen
    path('ordersen/', views.OrderSenListCreate.as_view(), name='ordersen-list'),
    path('ordersen/<int:pk>/', views.OrderSenDetail.as_view(), name='ordersen-detail'),

]
