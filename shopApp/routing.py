from django.urls import path,re_path

from .consumers import ShopConsumer

websocket_urlpatterns = [
    re_path('ws/user/(?P<user_id>\w+)', ShopConsumer.as_asgi())
]