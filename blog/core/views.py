from core.models import Category, Post, User
from django.shortcuts import render, HttpResponse

def index(request):
    categories = Category.objects.all()
    context = {
        'title': 'Блог Динары Шафигуллиной',
        'categories' : categories
    }
    return render(request,'/home/dinara/blog/blog/core/templates/index.html', context=context)


def show_category(request, category_id):
    categories = Category.objects.all()
    category_name = Category.objects.filter(id=category_id)
    posts = Post.objects.filter(categoryies=category_id)
    print(posts)
    context = {
        'title': 'Блог Динары Шафигуллиной',
        'categories' : categories,
        'category_name' : category_name,
        'posts' : posts,
    }
    return render(request, '/home/dinara/blog/blog/core/templates/category.html', context=context)