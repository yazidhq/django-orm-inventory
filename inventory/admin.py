from django.contrib import admin
from .models import Category, Product, Attribute, AttributeValue, Inventory, StockControl, Image

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Attribute)
# admin.site.register(AttributeValue)
# admin.site.register(Inventory)
# admin.site.register(StockControl)
# admin.site.register(Image)


class ProductImageInline(admin.TabularInline):
    model = Image


class StockControlInline(admin.TabularInline):
    model = StockControl


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue


@admin.register(Inventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, StockControlInline]


@admin.register(Attribute)
class ProductAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
