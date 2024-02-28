from django.forms import ModelForm
from news.models import News


class NewsCreateForm(ModelForm):
    class Meta:
        model = News
        fields =("header","text","image","user","category")
        exclude = ["user"]