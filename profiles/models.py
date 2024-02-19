from django.db import models
from shopApp.models import Product
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from orders.models import Order
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    date_of_birth=models.DateField()
    payment_card =models.CharField(max_length=20)
    walmart_cash = models.DecimalField(max_digits=13,decimal_places = 2, validators=[MinValueValidator(0)])
    cart =models.ManyToManyField(Product)
    address =models.CharField(max_length=250)
    phone_number = PhoneNumberField(blank = True)
    order_history =models.ManyToManyField(Order)
