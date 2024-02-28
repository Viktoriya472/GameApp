from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from ads.models import Ad
from ads.forms import AdForm
from django.urls import reverse_lazy


class AdsList(ListView):
    model = Ad
    template_name="ads/ads.html"
    context_object_name ="ads"
    ordering = ["-id"]
    paginate_by = 3


class AdsDetail(DetailView):
    model = Ad
    template_name = "ads/ad.html"
    context_object_name = "ad"


class AsdCreate(CreateView):
    model = Ad
    template_name =  "ads/ad_create.html"
    form_class = AdForm
    success_url = reverse_lazy("ads")


class AdsUpdate(UpdateView):
    model=Ad
    template_name = "ads/ad_create.html"
    form_class = AdForm
    success_url = reverse_lazy("ads")


class AdsDelete(DeleteView):
    template_name = "ads/ad_delete.html"
    queryset = Ad.objects.all()
    success_url = reverse_lazy("ads")
