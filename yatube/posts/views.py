# posts/views.py Версия от 8 февраля. Устранение замечаний Алексея Фролова
from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from yatube.settings import POSTS_PER_PAGE
from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
