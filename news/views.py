from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import NewsForm, RegisterForm

def home(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/home.html', {'news': news})


def category_view(request, category):
    news = News.objects.filter(category=category).order_by('-created_at')
    return render(request, 'news/category.html', {'news': news, 'category': category})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'news/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def add_news(request):
    form = NewsForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('/')
    return render(request, 'news/add_news.html', {'form': form})


@login_required
def my_news(request):
    news = News.objects.filter(author=request.user)
    return render(request, 'news/my_news.html', {'news': news})


@login_required
def edit_news(request, news_id):
    post = get_object_or_404(News, id=news_id, author=request.user)
    form = NewsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('/my-news/')
    return render(request, 'news/edit_news.html', {'form': form})


@login_required
def delete_news(request, news_id):
    post = get_object_or_404(News, id=news_id, author=request.user)
    post.delete()
    return redirect('/my-news/')


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    return render(request, 'news/register.html', {'form': form})