from core.models import Category, Post, User
from django.shortcuts import render, HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

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


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})

