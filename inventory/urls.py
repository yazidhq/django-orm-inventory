from django.urls import path
from . import views

urlpatterns = [
    # CATEGORY
    path('category/', views.category, name="category"),
    path('add_category/', views.add_category, name="add_category"),
    # path('view_category/<str:slug>', views.view_category, name="view_category"),
    # path('edit_category/<str:slug>', views.edit_category, name="edit_category"),
    # path('delete_category/<str:slug>', views.delete_category, name="delete_category"),

    # PRODUCTS
    path('products/', views.products, name="products"),
    path('view/<str:slug>', views.view, name="view"),
    path('edit/<str:slug>', views.edit, name="edit"),
    path('delete/<str:slug>', views.delete, name="delete"),
    path('add/', views.add, name="add"),
]