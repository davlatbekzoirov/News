from multiprocessing import context

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import Category, News
from .forms import ContactForm

def news_list(request):
    news_list = News.published.all()
    context = {
        'news_list': news_list,
    }
    return render(request, "news/news_list.html", context=context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.PUBLISHED)
    context = {
        'news': news,
    }

    return render(request, "news/news_detail.html", context=context)


def homePageView(request):
    news_list = News.published.all().order_by('-publish_time')
    categories = Category.objects.all()
    featured_news = news_list[:5]

    context = {
        'news_list': news_list,
        'featured_news': featured_news,
        'categories': categories,
    }
    return render(request, "news/home.html", context=context)

class HomePageView(ListView):
    model =News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = self.model.objects.all()
        context['news_list'] = self.model.published.all().order_by('-publish_time')
        context['featured_news'] = self.model.published.all().order_by('-publish_time')[:5]

        return context

class ContactPageView(TemplateView):
    template_name = "news/contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2> Thank You! </h2>")
        context = {
            'form': form,
        }
        return render(request, self.template_name, context=context)

def categoryPageView(request):
    return render(request, "news/category.html", context={})

class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'local_news'

class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

class AbroadNewsView(ListView):
    model = News
    template_name = 'news/abroad.html'
    context_object_name = 'abroad_news'

class TechnologyNewsView(ListView):
    model = News
    template_name = 'news/technology.html'
    context_object_name = 'technology_news'

class AvtoNewsView(ListView):
    model = News
    template_name = 'news/avto.html'
    context_object_name = 'avto_news'