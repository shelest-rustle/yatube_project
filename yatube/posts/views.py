from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Вы попали на главную страницу сайта! Если Вы её видете, то я молодец!')


def group_posts(request, slug):
    return HttpResponse(f'Здесь будет страница, на которой можно будет посмотреть посты, отфлильтрованные по {slug}. А пока что: ' 'Вы потрясающий!')