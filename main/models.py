from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField("Аватар", default="profile_images/default.jpg",
                               upload_to="profile_images/", blank=True)

    def __str__(self):
        return f'{self.user.username}'

    def save(self):
        super().save()
        img = Image.open(self.avatar.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.avatar.path, quality=90, optimize=True)

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
