from django.urls import path
from order import views

app_name = 'order'


urlpatterns = [
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('cart-view/', views.cart_view, name='cart'),
]


