from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    header = models.CharField("Заголовок", max_length=255)
    text = models.TextField("Текст")
    image = models.ImageField("Картинка")
    datetime = models.DateTimeField("Дата и время", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    category = models.ManyToManyField("Category",
                                      through="NewsCategory",
                                      verbose_name="Категория")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f'{self.header}'


class Category(models.Model):
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.name}'


class NewsCategory(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
