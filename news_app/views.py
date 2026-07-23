from django.shortcuts import render, get_object_or_404
from unicodedata import category

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


def homePageView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'categories': categories,
    }

    return render(request, "news/home.html", context=context)

def contactPageView(request):
    return render(request, "news/contact.html", context={})

def categoryPageView(request):
    return render(request, "news/category.html", context={})