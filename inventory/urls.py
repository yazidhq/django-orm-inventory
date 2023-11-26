from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="all_products"),
    path('view/<str:slug>', views.view, name="view"),
    path('edit/<str:slug>', views.edit, name="edit"),
    path('delete/<str:slug>', views.delete, name="delete"),
]