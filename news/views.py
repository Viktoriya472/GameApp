from django.views.generic import ListView, DetailView, CreateView, \
      UpdateView, DeleteView
from news.models import News
from news.forms import NewsCreateForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy


class NewsList(ListView):
    model = News
    template_name = "news/news.html"
    context_object_name = "all_news"
    ordering = ["-id"]


class NewsDetail(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news"


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
