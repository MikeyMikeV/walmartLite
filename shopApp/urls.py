from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('category-list/', views.cat_list, name='cat_list'),
    path('category/<int:cid>/', views.category, name='category'),
    path('category/specific/<int:cid>/', views.sub_category, name='sub_category'),
    path('category/specific/<int:cid>/<int:bid>/', views.brand_products, name='brand_products'),
    path('category/product/<int:pid>/', views.product_detail, name='product_detail'),
]
