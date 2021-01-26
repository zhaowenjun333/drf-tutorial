from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Shipment ,HouseBill,Package,ServiceCode,ShipmentCommodity


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):...
    # list_display = "__all__"
    # search_fields = list_display
    # list_filter = list_display

@admin.register(HouseBill)
class HouseBillAdmin(admin.ModelAdmin):...
    # list_display = "__all__"
    # search_fields = list_display
    # list_filter = list_display


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):...
    # list_display = "__all__"
    # search_fields = list_display
    # list_filter = list_display

@admin.register(ServiceCode)
class ServiceCodeAdmin(admin.ModelAdmin):...
    # list_display = "__all__"
    # search_fields = list_display
    # list_filter = list_display

@admin.register(ShipmentCommodity)
class ShipmentCommodityAdmin(admin.ModelAdmin): ...
# list_display = "__all__"
# search_fields = list_display
# list_filter = list_display