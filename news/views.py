from django.views.generic import ListView,DetailView,CreateView
from news.models import News
from news.forms import NewsCreateForm

class NewsList(ListView):
    model=News
    template_name = "news/news.html"
    context_object_name = "all_news"
    ordering = ["-id"]

class NewsDetail(DetailView):
    model = News
    template_name ="news/news_detail.html"
    context_object_name ="news"


class NewsCreate(CreateView):
    model = News
    template_name =""
    form_class =NewsCreateForm