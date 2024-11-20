from rest_framework import serializers
from django.contrib.auth.models import User
from news.models import News, Category
from ads.models import Ad, Game, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GameSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class AdSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class CommentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['active']
