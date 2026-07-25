from .models import News, Category

def tranding_news(request):
    news_list = News.published.order_by('-publish_time')[:4]
    categories = Category.objects.all()
    context = {
        'tranding_news': news_list,
        'categories': categories
    }
    return context