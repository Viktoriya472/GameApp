from django.urls import path
from main.views import ProfileView, ProfileUpdate, ContactView


urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile_update/<int:pk>/', ProfileUpdate.as_view(),
         name='profile_update'),
    path('', ContactView.as_view(), name='contact'),
]
