from django.contrib import admin
from .models import ProductCategories, Product

# Register your models here.

class AdminProductCategories(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') 

class AdminProduct(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(ProductCategories, AdminProductCategories)
admin.site.register(Product, AdminProduct)