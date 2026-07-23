from django.shortcuts import render, get_object_or_404
from .models import Category, News

def news_list(request):
    news_list = News.published.all()
    context = {
        'news_list': news_list,
    }
    return render(request, "news/news_list.html", context=context)

def news_detail(request, id):
    news = get_object_or_404(News, pk=id, status=News.Status.PUBLISHED)
    context = {
        'news': news,
    }

    return render(request, "news/news_detail.html", context=context)