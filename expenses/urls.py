from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.ExpenseListView.as_view(),
        name="expense-list"
    ),
    path(
        "expense/<int:pk>",
        views.ExpenseDetailView.as_view(),
        name="expense-detail"
    ),
    path(
        "create",
        views.ExpenseCreateView.as_view(),
        name="expense-create"
    ),
    path(
        "expense/<int:pk>/update",
        views.ExpenseUpdateView.as_view(),
        name="expense-update",
    ),
    path(
        "expense/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="expense-delete",
    ),
    path(
        "by-name",
        views.ExpenseOrderByName.as_view(),
        name="expense-order-by-name"
    ),
    path(
        "by-name-desc",
        views.ExpenseOrderByNameDesc.as_view(),
        name="expense-order-by-name-desc"
    ),
    path(
        "by-category",
        views.ExpenseOrderByCategory.as_view(),
        name="expense-order-by-category"
    ),
    path(
        "by-category-desc",
        views.ExpenseOrderByCategoryDesc.as_view(),
        name="expense-order-by-category-desc"
    ),
    path(
        "by-price",
        views.ExpenseOrderByPrice.as_view(),
        name="expense-order-by-price"
    ),
    path(
        "by-price-desc",
        views.ExpenseOrderByPriceDesc.as_view(),
        name="expense-order-by-price-desc"
    ),
    path(
        "by-date",
        views.ExpenseOrderByDate.as_view(),
        name="expense-order-by-date"
    ),
    path(
        "by-date-desc",
        views.ExpenseOrderByDateDesc.as_view(),
        name="expense-order-by-date-desc"
    ),
    url(r'^search/$', views.search, name='search'),
]
