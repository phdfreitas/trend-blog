from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import UpdateUserForm


class NewUser(generic.CreateView):
    form_class = UpdateUserForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/new-user.html'
