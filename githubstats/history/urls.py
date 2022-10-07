from django.urls import path

from . import views

app_name = 'history'

urlpatterns = [
    path('header/', views.HeaderView.as_view(), name='header'),
]
