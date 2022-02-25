from urllib.parse import urlparse
from django.urls import path
from . import views

app_name="cart"

urlpatterns = [
    path('add/<int:product_id>/', views.add_product, name="add"),
    path('delete/<int:product_id>/', views.delete_product, name="delete"),
    path('remove/<int:product_id>/', views.remove_product, name="remove"),
    path('empty/<int:product_id>/', views.empty_cart, name="empty")
]