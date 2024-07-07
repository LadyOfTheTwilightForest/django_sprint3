from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseNotFound
from django.utils import timezone

from .models import Post, Category

POSTS_PER_PAGE = 5


def get_published_posts():
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )


def index(request):
    template = 'blog/index.html'
    posts = get_published_posts().select_related(
        'category', 'location', 'author'
    )[:POSTS_PER_PAGE]
    context = {
        'post_list': posts,
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        get_published_posts(),
        pk=id
    )
    context = {
        'post': post,
    }
    return render(request, template, context)


def category_posts(request, slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(
            slug=slug,
            is_published=True,
        ),
    )

    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category=category,
    ).select_related('category', 'location', 'author')

    data = {
        'category': category,
        'post_list': posts,
    }
    return render(request, template, context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
