# home/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('ask/', views.ask_me_anything, name='ask_me_anything'),
]

# urlpatterns = [
#     path('', views.index, name='Home'),
#     path('about/', views.about, name='about'),
#     path('services/', views.services, name='services'),
#     path('contact/', views.contact, name='contact'),
#     path('ask-me-anything/', views.ask_me_anything, name='ask_me_anything'),
# ]



    
