from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import Product
from profiles.models import Profile

class ShopConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = None
        self.profile = None
        self.profile_group_name = None

    def connect(self):
        self.user_id = self.scope['user'].pk
        self.user_group_name = f'user_{self.user_id}'
        self.profile = Profile.objects.get(user_id = self.user_id)

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.user_group_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.user_group_name,
            self.channel_name,
        )
    
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        match message:
            case 'add_cart':
                product = Product.objects.get(pk = text_data_json['product_id'])
                self.profile.cart.add(product)
            case 'plus_count':
                pass
            case 'minus_count':
                pass
            case 'clear_product':
                pass
            case _:
                print('Non')