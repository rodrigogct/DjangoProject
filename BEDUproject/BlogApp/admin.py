from django.contrib import admin
from .models import Category, Post

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AdminPost(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)