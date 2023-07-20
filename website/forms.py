from .models import *
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['category', 'deadline', 'title', 'task', 'special_requirement', 'file']