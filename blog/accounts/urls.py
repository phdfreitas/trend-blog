from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar', views.NewUser.as_view(), name='newUser'),
]