from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:uid>/', views.profile_detail, name='profile_detail'),
    path('<int:uid>/add_address/', views.add_address, name='add_address')
]