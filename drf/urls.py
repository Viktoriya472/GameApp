from django.urls import path
from drf.views import UserList, UserDetail, NewsList, NewsDetail, \
    NewsCategoryList, NewsCategoryDetail, GameList, GameDetail, AdList, \
    AdDetail, CommentList, CommentDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('news/', NewsList.as_view()),
    path('news/<int:pk>', NewsDetail.as_view()),
    path('news_category/', NewsCategoryList.as_view()),
    path('news_category/<int:pk>', NewsCategoryDetail.as_view()),
    path('game/', GameList.as_view()),
    path('game/<int:pk>', GameDetail.as_view()),
    path('ad/', AdList.as_view()),
    path('ad/<int:pk>', AdDetail.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/<int:pk>', CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
