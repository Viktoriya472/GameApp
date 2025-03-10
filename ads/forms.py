from django.forms import ModelForm
from ads.models import Ad, Comment
from django import forms


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ('title', 'content_upload', 'game')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5,
                                          'placeholder': 'Комментарий'}),
        }
