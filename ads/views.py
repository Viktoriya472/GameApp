from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from ads.models import Ad, Comment
from ads.forms import AdForm, CommentForm
from django.contrib.auth.models import User 
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, Template


class AdsList(ListView):
    model = Ad
    template_name="ads/ads.html"
    context_object_name ="ads"
    ordering = ["-id"]
    paginate_by = 3


class AdsDetail(FormMixin, DetailView):
    model = Ad
    template_name = "ads/ad.html"
    context_object_name = "ad"
    form_class=CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(ad=self.kwargs['pk'],active=True)
        return context
    
    def post(self,request,*args,**kwargs):
        form=CommentForm(request.POST)
        if form.is_valid():
            ad = self.get_object()
            form.instance.ad = ad
            form.instance.user = User.objects.get(username=request.user)
            form.save()    
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_success_url(self, **kwargs):
            return reverse_lazy('ad_detail',kwargs={'pk':self.get_object().pk})
    

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


class Comments(TemplateView):
    model = Comment
    template_name = "ads/comments.html"
    context_object_name = "comments"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(ad=Ad.objects.get(user=self.request.user),active=False)
        return context
    

def updateComment(request,pk,type):
    comment = Comment.objects.get(pk=pk)
    if type == "public":
        comment.active = True
        comment.save()
        template = Template('''<div class="post_content"><p>Комментарий опубликован.</p></div>''')
        context = Context({'comment':comment})
        return HttpResponse(template.render(context))
    elif type == "delete":
        comment.delete()
        template = Template('''<div class="post_content"><p>Комментарий удален.</p></div>''')
        context = Context({'comment':comment})
        return HttpResponse(template.render(context))
    return reverse_lazy("comments")