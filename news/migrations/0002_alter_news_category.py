# Generated by Django 5.0.2 on 2024-02-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ManyToManyField(through='news.NewsCategory', to='news.category', verbose_name='Категория'),
        ),
    ]