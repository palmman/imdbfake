from django import urls
from django.urls import path, include
from . import views


urlpatterns = [

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),

    path('profiles/', views.profiles, name='profiles'),
    path('edit_profile/', views.editProfile, name='edit_profile'),
]

