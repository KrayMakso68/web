from django.shortcuts import render
from .models import Articles

# Create your views here.
def news_index(request):
    news = Articles.objects.order_by('-data')
    data = {
        'title': 'Новости',
        'news' : news,
    }
    return render(request, 'news/news_home.html', data)

def create(request):
    data = {
        'title' : 'Создание новости',

    }
    return render(request, 'news/create.html', data)