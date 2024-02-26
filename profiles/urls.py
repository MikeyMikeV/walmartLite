from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile_detail, name='profile_detail'),
    path('add_address/', views.add_address, name='add_address')
]