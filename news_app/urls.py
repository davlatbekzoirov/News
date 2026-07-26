from django.urls import path
from .views import news_list, news_detail, homePageView, ContactPageView, categoryPageView, HomePageView, \
    LocalNewsView, SportNewsView, AbroadNewsView, TechnologyNewsView, AvtoNewsView, \
    NewsUpdateView, NewsDeleteView, NewsCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('category/', categoryPageView, name='category_page'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('local-news/', LocalNewsView.as_view(), name='local_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page'),
    path('abroad-news/', AbroadNewsView.as_view(), name='abroad_news_page'),
    path('technology-news/', TechnologyNewsView.as_view(), name='technology_news_page'),
    path('avto-news/', AvtoNewsView.as_view(), name='avto_news_page'),
]