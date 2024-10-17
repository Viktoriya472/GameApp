from rest_framework import serializers
from django.contrib.auth.models import User
from news.models import News, Category
from ads.models import Ad, Game, Comment
# from django.contrib.auth.hashers import make_password


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=150)
#     first_name = serializers.CharField(allow_blank=True, max_length=150)
#     last_name = serializers.CharField(allow_blank=True, max_length=150)
#     email = serializers.CharField(max_length=254)
#     password = serializers.CharField(write_only=True, required=True, max_length=128)

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data.get(
#             'password'))
#         return super(User, self).create(validated_data)

#     def update(self, validated_data):
#         validated_data['password'] = make_password(validated_data.get(
#             'password'))
#         return super(User, self).update(validated_data)

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
        # fields = '__all__'
        exclude = ['active']
