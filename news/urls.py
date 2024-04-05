from django.urls import path
from news.views import NewsList,NewsDetail,NewsCreate,NewsUpdate,NewsDelete


urlpatterns = [
    path('news/',NewsList.as_view(),name='news'),
    path('<int:pk>/',NewsDetail.as_view(),name='news_detail'),
    path('create/',NewsCreate.as_view(),name='news_create'),
    path('<int:pk>/update/',NewsUpdate.as_view(),name='news_update'),
    path('<int:pk>/delete/',NewsDelete.as_view(),name='news_delete'),
    
]
