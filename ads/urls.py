from django.urls import path
from ads.views import AdsList,AdsDetail,AsdCreate,AdsUpdate,AdsDelete,Comments,updateComment


urlpatterns = [
    path('',AdsList.as_view(),name="ads"),
    path('<int:pk>/',AdsDetail.as_view(),name="ad_detail"),
    path('create/',AsdCreate.as_view(),name="ad_create"),
    path('<int:pk>/update/', AdsUpdate.as_view(),name="ad_update"),
    path('<int:pk>/delete',AdsDelete.as_view(),name="ad_delete"),
    path('comments/', Comments.as_view(), name = 'comments'),
    path('update_comment_active/<int:pk>/<slug:type>',updateComment,name="update_comment"),
]
