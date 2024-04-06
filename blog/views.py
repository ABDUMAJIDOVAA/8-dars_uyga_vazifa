'''CRUD'''

# C - Create
# R - Read
# U - Update
# D - Delete


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from django.http import HttpResponse

from .models import Post, Category
from .forms import PostForm, LoginForm, RegisterForm

# Create your views here.



def all_posts(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'title': "Barcha Retseptlar"
    }
    return render(request, 'blog/index.html', context=context)


def posts_by_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'categories': categories,
        'title': f"{category.title} ga tegishli retseptlar"
    }
    return render(request, 'blog/index.html', context=context)


# Read
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.views += 1
    post.save()
    context = {
        'post': post,
        "title": post.title
    }
    return render(request, 'blog/detail.html', context=context)


def post_create(request):

    form = PostForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        messages.success(request, "Maqola muvaffaqiyatli saqlandi!!!")
        form.save()

    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/post_form.html', context=context)


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(data=request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Retsept muvaffaqiyatli o'zgartirildi!!!")
        return redirect('post_detail', pk=pk)
    context = {
        'form': form
    }
    return render(request, 'blog/post_form.html', context)


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Retsept muvaffaqiyatli o'chirildi!!!")
        return redirect('index')

    context = {
        'post': post
    }
    return render(request, 'blog/post_delete.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Saytga xush kelibsiz! {user.username}")
            return redirect('index')

        if form.errors:
            for error in form.error_messages.values():
                messages.error(request, str(error))

    # form = LoginForm()
    # context = {
    #     'form': form
    # }
    return render(request, 'blog/user_login.html')


def user_logout(request):
    logout(request)
    messages.warning(request, "Siz saytdan chiqdingiz!!!")
    return redirect('login')


def user_register(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')

    form = RegisterForm()
    context = {
        'form': form,
        'title': "Registratsiya"
    }
    return render(request, 'blog/register.html', context)