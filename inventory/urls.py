from django.urls import path
from . import views

urlpatterns = [
    # INDEX DASHBOARD
    path('', views.dashboard, name="dashboard"),

    # CATEGORY
    path('category/', views.category, name="category"),
    path('add_category/', views.add_category, name="add_category"),
    path('delete_category/<str:slug>', views.delete_category, name="delete_category"),
    path('edit_category/<str:slug>', views.edit_category, name="edit_category"),

    # PRODUCTS
    path('products/', views.products, name="products"),
    path('view/<str:slug>', views.view, name="view"),
    path('edit/<str:slug>', views.edit, name="edit"),
    path('delete/<str:slug>', views.delete, name="delete"),
    path('add/', views.add, name="add"),

    # ATTRIBUTES
    path('attribute/', views.attribute, name="attribute"),
    path('view_attribute/<int:id>', views.view_attribute, name="view_attribute"),
    path('add_attribute/', views.add_attribute, name="add_attribute"),
    path('add_attribute_value/', views.add_attribute_value, name="add_attribute_value"),
    path('delete_attr/<int:id>', views.delete_attr, name="delete_attr"),
]