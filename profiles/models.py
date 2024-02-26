from django.db import models
from shopApp.models import Product
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from orders.models import Order
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    date_of_birth=models.DateField(blank = True, null = True)
    payment_card =models.CharField(max_length=20, blank = True, null = True)
    walmart_cash = models.DecimalField(max_digits=13,decimal_places = 2, validators=[MinValueValidator(0)], default = 0)
    cart =models.ManyToManyField(Product, blank = True, null = True)
    address =models.CharField(max_length=250, blank = True, null = True)
    phone_number = PhoneNumberField(blank = True)
    order_history =models.ManyToManyField(Order, blank = True, null = True)

    def __str__(self):
        return f'{self.user.username}\'s profile'

class Address(models.Model):
    address = models.CharField(max_length = 100,)
    appartments = models.CharField(max_length = 20,blank = True, null = True)
    city = models.CharField(max_length = 30,)
    state = models.CharField(max_length = 30,)
    zip_code = models.CharField(max_length = 20,)
    notes = models.CharField(max_length = 250,blank = True, null = True)
    current_address = models.BooleanField(default=True)

from django.dispatch import receiver

@receiver(models.signals.post_save, sender = User)
def auto_delete_file_on_delete(sender, instance:User, **kwargs):
    Profile.objects.create(user = instance)