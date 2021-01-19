from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Post


class HomeView(TemplateView):
    template_name = 'post/home.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'author', 'status']
    template_name = 'post/new-post.html'


class PostListView(ListView):
    model = Post
    template_name = 'post/list-posts.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail-post.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'status']
    template_name = 'post/update-post.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/delete-post.html'
    success_url = reverse_lazy('listPosts')