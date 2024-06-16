from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseNotFound, Http404
from django.utils import timezone

from .models import Post, Category

def index(request):
    template = 'blog/index.html'
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    ).order_by('-pub_date')[:5]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post, id=id)
    if post.pub_date > timezone.now() or not post.is_published or not post.category.is_published:
        return Http404()

    context = {
        'post': post,
        'location': post.location
    }
    # if id not in post_dict:
    #     raise Http404()
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, category_slug=category_slug)

    if not category.is_published:
        return Http404()
    
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category=category,
    ).order_by('-pub_date')

    data = {
        'category': category,
        'posts': posts,
    }
    return render(request, template, context=data)



def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
