from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField("Название",max_length=100)

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

class Ad(models.Model):
    title = models.CharField("Заголовок", max_length=300)
    content_upload = RichTextUploadingField("Текст", blank=True,null=True)
    datetime = models.DateTimeField("Дата и время",auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Пользователь")
    game = models.ForeignKey(Game,on_delete=models.CASCADE,verbose_name="Игра")

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        