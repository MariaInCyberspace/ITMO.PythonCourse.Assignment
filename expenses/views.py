from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from . import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Expense


class ExpenseListView(ListView):
    model = Expense
    queryset = Expense.objects.all()


class ExpenseOrderByName(ListView):
    model = Expense
    queryset = Expense.objects.all().order_by("name")


class ExpenseOrderByCategory(ListView):
    model = Expense
    queryset = Expense.objects.all().order_by("category")


class ExpenseOrderByPrice(ListView):
    model = Expense
    queryset = Expense.objects.all().order_by("price")


class ExpenseOrderByDate(ListView):
    model = Expense
    queryset = Expense.objects.all().order_by("date")


class ExpenseDetailView(DetailView):
    model = Expense


class ExpenseCreateView(SuccessMessageMixin, CreateView):
    model = Expense
    form_class = forms.ExpenseForm
    success_url = reverse_lazy("expense-list")
    success_message = "Your new expense entry was created!"


class ExpenseUpdateView(SuccessMessageMixin, UpdateView):
    model = Expense
    form_class = forms.ExpenseForm
    success_message = "Your expense entry was updated!"
    success_url = reverse_lazy("expense-list")
    # def get_success_url(self):
    #     return reverse_lazy(
    #         "expense-detail",
    #         kwargs={"pk": self.expense.id}
    #     )


class EntryDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy("expense-list")
    success_message = "Your expense entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


