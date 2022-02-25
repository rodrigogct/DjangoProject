from django.shortcuts import render
from BlogApp.models import Post, Category

# Create your views here.

def blog(request):

    posts = Post.objects.all()
    return render(request, "blog.html", {"posts": posts})

def category(request, categories_id):

    category = Category.objects.get(id=categories_id)
    posts = Post.objects.filter(categories = category)
    return render(request, "categories.html", {"category": category, "posts": posts})