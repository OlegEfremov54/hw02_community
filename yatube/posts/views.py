# posts/views.py Версия от 3 февраля. Финиш
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': 'Главная страница проекта'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    text = f'Записи сообщества {group.title}'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'text': text,
        'title': 'Страница сообществ'
    }
    return render(request, 'posts/group_list.html', context)
