from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField("Аватар", default="profile_images/default.jpg",
                               upload_to="profile_images/", blank=True)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Contact(models.Model):
    email = models.EmailField("")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
