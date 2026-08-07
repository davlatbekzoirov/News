from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from .custom_permissions import OnlyLoggedSuperUser
from .models import Category, News
from .forms import ContactForm, CommentForm
from accounts.models import Profile

def news_list(request):
    news_list = News.published.all()
    context = {
        'news_list': news_list,
    }
    return render(request, "news/news_list.html", context=context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.PUBLISHED)
    comments = news.comments.filter(active=True)
    new_comment = None

    profile_image = None
    if request.user.is_authenticated:
        profile_image = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()
            return redirect(news.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'news': news,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'profile_image': profile_image,
    }
    return render(request, "news/single.html", context=context)

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

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')
        return news

class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news

class AbroadNewsView(ListView):
    model = News
    template_name = 'news/abroad.html'
    context_object_name = 'abroad_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Xorij')
        return news

class TechnologyNewsView(ListView):
    model = News
    template_name = 'news/technology.html'
    context_object_name = 'technology_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Texnologiya')
        return news

class AvtoNewsView(ListView):
    model = News
    template_name = 'news/avto.html'
    context_object_name = 'avto_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Avto')
        return news

class NewsUpdateView(OnlyLoggedSuperUser, UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_edit.html'

class NewsDeleteView(OnlyLoggedSuperUser, DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')

class NewsCreateView(OnlyLoggedSuperUser, CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = '__all__'

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_page_view(request):
    admin_user = User.objects.filter(is_superuser=True)
    context = {
        'admin_users': admin_user,
    }
    return render(request, 'pages/admin_page.html', context=context)


class SearchResultsView(ListView):
    model = News
    template_name = 'news/search_result.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(Q(title__icontains=query)|Q(body__icontains=query))
