from unicodedata import name
from django.db import models

# Create your models here.

class ProductCategories(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "productCategory"
        verbose_name_plural = "productsCategory"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    categories = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store')
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
    