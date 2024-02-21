from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address','appartments','city', 'state','zip_code','notes')