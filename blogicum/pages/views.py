from django.shortcuts import render

from django.http import HttpResponseNotFound


def about(request):
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    template = 'pages/rules.html'
    return render(request, template)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
