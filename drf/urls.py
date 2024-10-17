from django.urls import path
from drf.views import UserList, UserDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
