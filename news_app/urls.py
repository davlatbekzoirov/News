from django.urls import path
from .views import news_list, news_detail, homePageView, ContactPageView, categoryPageView, HomePageView, \
    LocalNewsView, SportNewsView, AbroadNewsView, TechnologyNewsView, AvtoNewsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('category/', categoryPageView, name='category_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('local-news/', LocalNewsView.as_view(), name='local_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page'),
    path('abroad-news/', AbroadNewsView.as_view(), name='abroad_news_page'),
    path('technology-news/', TechnologyNewsView.as_view(), name='technology_news_page'),
    path('avto-news/', AvtoNewsView.as_view(), name='avto_news_page'),
]