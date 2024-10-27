from django.contrib import admin

from .models import Price, Product, Type


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "barcode", "updated_at", "type", "price")
    search_fields = ("name", "barcode")
    list_filter = ("type", "updated_at")


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("amount", "currency")
