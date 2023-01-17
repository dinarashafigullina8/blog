from core.models import Category, Post, User
from django.shortcuts import render, HttpResponse

def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {
        'title': 'Блог Динары Шафигуллиной',
        'categories' : categories,
        'posts' : posts
    }
    return render(request,'/home/dinara/blog/blog/core/templates/index.html', context=context)


def show_category(request, category_id):
    categories = Category.objects.all()
    category_name = Category.objects.filter(id=category_id)
    posts = Post.objects.filter(categoryies=category_id)
    context = {
        'title': 'Блог Динары Шафигуллиной',
        'categories' : categories,
        'category_name' : category_name.first(),
        'posts' : posts,
    }
    return render(request, '/home/dinara/blog/blog/core/templates/category.html', context=context)


def read_post(request, post_id):
    categories = Category.objects.all()
    post = Post.objects.filter(id=post_id)
    print(post)
    context = {
        'title': 'Блог Динары Шафигуллиной',
        'categories' : categories,
        'post' : post.first()
    }
    return render(request, '/home/dinara/blog/blog/core/templates/post.html', context=context)