from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Category, News
from .forms import ContactForm

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
    news_list = News.published.all()
    categories = Category.objects.all()
    featured_news = news_list[:5]

    context = {
        'news_list': news_list,
        'featured_news': featured_news,
        'categories': categories,
    }
    return render(request, "news/home.html", context=context)

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