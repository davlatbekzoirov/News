from .models import News

def tranding_news(request):
    news_list = News.published.order_by('-publish_time')[:10]
    context = {
        'tranding_news': news_list
    }
    return context