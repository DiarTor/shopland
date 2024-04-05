from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.single_post, name='post-detail-page')
]