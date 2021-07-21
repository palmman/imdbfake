from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<slug:slug>', views.detail, name='detail'),
    path('director/<slug:slug>', views.director, name='director'),
    # path('search/', views.search, name='search'),
]
