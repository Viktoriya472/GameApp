from django.views.generic import ListView, DetailView, CreateView, \
      UpdateView, DeleteView, TemplateView
from ads.models import Ad, Comment
from ads.forms import AdForm, CommentForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.template import Context, Template
from django.db.models import Q
# from django.contrib.postgres.search import SearchVector,SearchQuery, \
# SearchRank


class AdsList(ListView):
    model = Ad
    template_name = "ads/ads.html"
    context_object_name = "ads"
    ordering = ["-id"]
    paginate_by = 7


class AdsDetail(FormMixin, DetailView):
    model = Ad
    template_name = "ads/ad.html"
    context_object_name = "ad"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(ad=self.kwargs['pk'],
                                                     active=True)
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            ad = self.get_object()
            form.instance.ad = ad
            form.instance.user = User.objects.get(username=request.user)
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('ad_detail', kwargs={'pk': self.get_object().pk})


class AsdCreate(CreateView):
    model = Ad
    template_name = "ads/ad_create.html"
    form_class = AdForm
    success_url = reverse_lazy("ads")

    def post(self, request, *args, **kwargs):
        form = AdForm(request.POST)
        if form.is_valid():
            form.instance.user = User.objects.get(username=request.user)
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class AdsUpdate(UpdateView):
    model = Ad
    template_name = "ads/ad_create.html"
    form_class = AdForm
    success_url = reverse_lazy("ads")


class AdsDelete(DeleteView):
    template_name = "ads/ad_delete.html"
    queryset = Ad.objects.all()
    success_url = reverse_lazy("ads")


class Comments(TemplateView):
    model = Comment
    template_name = "ads/comments.html"
    context_object_name = "comments"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            ad__user=self.request.user, active=False)
        return context


def updateComment(request, pk, type):
    comment = Comment.objects.get(pk=pk)
    if type == "public":
        comment.active = True
        comment.save()
        template = Template('''<div class="post_content">
                            <p>Комментарий опубликован.</p></div>''')
        context = Context({'comment': comment})
        return HttpResponse(template.render(context))
    elif type == "delete":
        comment.delete()
        template = Template('''<div class="post_content">
                            <p>Комментарий удален.</p></div>''')
        context = Context({'comment': comment})
        return HttpResponse(template.render(context))
    return reverse_lazy("comments")


class Search(ListView):
    template_name = "ads/ads.html"
    context_object_name = "ads"
    ordering = ["-id"]

    def get_queryset(self):
        query = self.request.GET.get("q")
        # search_vector = SearchVector("title","content_upload","game__name")
        # search_query = SearchQuery(query)
        # return (Ad.objects.annotate(search=search_vector, \
        # rank=SearchRank(search_vector,search_query)).filter(search=search_query).order_by("-rank"))
        return Ad.objects.filter(Q(title__icontains=query) |
                                 Q(content_upload__icontains=query) |
                                 Q(game__name__icontains=query))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get("q")
        return context
