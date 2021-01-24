from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import BussinessPart


@admin.register(BussinessPart)
class BussinessPartAdmin(admin.ModelAdmin):pass
    # list_display ="__all__"
    # search_fields = list_display
    # list_filter = list_display
