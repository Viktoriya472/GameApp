# Generated by Django 5.0.2 on 2024-05-29 13:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_comment_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='comments_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
