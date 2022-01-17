from django.forms import NumberInput

from .models import Expense
import django_filters


class ExpenseFilter(django_filters.FilterSet):
    date_from = django_filters.DateTimeFilter(lookup_expr="gte", field_name='date', widget=NumberInput(attrs={'type': 'date'}))
    date_to = django_filters.DateTimeFilter(lookup_expr="lte", field_name='date', widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Expense
        fields = ['category']
