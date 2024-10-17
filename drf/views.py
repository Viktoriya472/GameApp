from rest_framework import mixins, generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, NewsSerializer, NewsCategorySerializer, AdSerialiser, GameSerialiser, CommentSerialiser
from ads.models import Ad, Game, Comment
from news.models import News, Category


# class UserList(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                generics.GenericAPIView):
#     queryset = User.objects.all().order_by('-id')
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class UserDetail(mixins.RetrieveModelMixin,
#                  mixins.UpdateModelMixin,
#                  mixins.DestroyModelMixin,
#                  generics.GenericAPIView):
#     queryset = User.objects.all().order_by('-id')
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)      

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer


class NewsCategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = NewsCategorySerializer


class NewsCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = NewsCategorySerializer


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all().order_by('-id')
    serializer_class = GameSerialiser


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all().order_by('-id')
    serializer_class = GameSerialiser


class AdList(generics.ListCreateAPIView):
    queryset = Ad.objects.all().order_by('-id')
    serializer_class = AdSerialiser


class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all().order_by('-id')
    serializer_class = AdSerialiser


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerialiser


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerialiser
