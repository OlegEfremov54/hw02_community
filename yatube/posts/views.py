# posts/views.py Версия от 8 февраля. Устранение замечаний Алексея Фролова
from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from yatube.settings import POSTS_PER_PAGE
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group.all()
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    title = f'Профайл пользователя {username}'
    author = get_object_or_404(User, username=username)
    posts = author.posts.select_related('group', 'author')
    page_number = request.GET.get('page')
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_obj = paginator.get_page(page_number)
    post_count = Post.objects.count()
    context = {
        'post_count': post_count,
        'page_obj': page_obj,
        'username': author,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post = get_object_or_404(Post, pk=post_id)
    post_count = Post.objects.count()
    title = f' Пост {post.text[:30]}'
    context = {
        'post': post,
        'post_count': post_count,
        'title': title,
    }
    return render(request, 'posts/post_detail.html', context)
