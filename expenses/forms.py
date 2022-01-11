from django import forms
from django.forms import ModelForm

from .models import Expense


class DateInput(forms.DateInput):
    input_type = 'date'


class ExpenseForm(ModelForm):

    class Meta:
        model = Expense
        fields = ['name', 'category', 'price', 'date', 'description']
        widgets = {
            'date': DateInput(),
        }