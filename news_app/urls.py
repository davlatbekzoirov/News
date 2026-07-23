from django.urls import path
from .views import news_list, news_detail, homePageView, contactPageView, categoryPageView

urlpatterns = [
    path('', homePageView, name='home_page'),
    path('contact-us/', contactPageView, name='contact_page'),
    path('category/', categoryPageView, name='category_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<int:id>/', news_detail, name='news_detail_page'),
]