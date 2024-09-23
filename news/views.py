from django.views.generic import ListView, DetailView, CreateView, \
      UpdateView, DeleteView
from news.models import News
from news.forms import NewsCreateForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models import Count


class NewsList(ListView):
    model = News
    template_name = "news/news.html"
    context_object_name = "all_news"
    ordering = ["-id"]


class NewsDetail(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        news_tags_ids = News.objects.values_list('id', flat=True)
        similar_news = News.objects.filter(tags__in=news_tags_ids
                                           ).exclude(id=self.get_object().id)
        context['similar_news'] = similar_news.annotate(
            same_tags=Count('tags')).order_by('-same_tags', '-id')[:4]
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    model = News
    template_name = "news/news_create.html"
    form_class = NewsCreateForm
    permission_required = "news.view_news"
    success_url = reverse_lazy("news")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    model = News
    template_name = "news/news_create.html"
    form_class = NewsCreateForm
    permission_required = "news.view_news"

    def get_success_url(self, **kwargs):
        return reverse_lazy("news_detail", kwargs={"pk": self.get_object().pk})


class NewsDelete(PermissionRequiredMixin, DeleteView):
    template_name = "news/news_delete.html"
    queryset = News.objects.all()
    permission_required = "news.view_news"
    success_url = reverse_lazy("news")


class Search(ListView):
    template_name = "news/news.html"
    context_object_name = "all_news"
    ordering = ["-id"]

    def get_queryset(self):
        query = self.request.GET.get("q")
        return News.objects.filter(Q(header__icontains=query) |
                                   Q(text__icontains=query) |
                                   Q(tags__name__icontains=query) |
                                   Q(category__name__icontains=query))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get("q")
        return context
