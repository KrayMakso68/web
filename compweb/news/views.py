from django.shortcuts import render

# Create your views here.
def news_index(request):
    data = {
        'title': 'Новости',
    }
    return render(request, 'news/news_home.html', data)