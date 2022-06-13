from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница лучшей соцсети кагорты!')


def group_posts(request, slug):
    return HttpResponse('Посты блогеров. Можно отфильтровать по группам.')
