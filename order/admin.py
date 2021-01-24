from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Order ,OrderItems


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):...
    # list_display = "__all__"
    # search_fields = list_display
    # list_filter = list_display

@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):...
    # list_display = "__all__"
    # search_fields = list_display
    # list_filter = list_display
