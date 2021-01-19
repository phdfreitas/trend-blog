from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('allPosts', views.PostListView.as_view(), name='listPosts'),
    path('newPost', views.PostCreateView.as_view(), name='newPost'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='detailPost'),
    path('<slug:slug>/update', views.PostUpdateView.as_view(), name='updatePost'),
    path('<slug:slug>/delete', views.PostDeleteView.as_view(), name='deletePost')
]