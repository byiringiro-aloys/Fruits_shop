from django.contrib import admin
from .models import Product, Offers


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock" )


class OrderAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")


admin.site.register(Product, ProductAdmin)
admin.site.register(Offers, OrderAdmin)