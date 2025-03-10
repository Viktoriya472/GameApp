from django.urls import path
from news.views import NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, Search


urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('news/search/', Search.as_view(), name='news_search'),

]
