from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchVideoView.as_view(), name='search video'),
    path('', views.AllVideosView.as_view(), name='get all videos'),
]
