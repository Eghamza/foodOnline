from django.contrib import admin
from .models import Vendor,OpeningHours

# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor_name', 'is_approved', 'created_at')
    list_editable=('vendor_name', 'is_approved')

admin.site.register(Vendor, VendorAdmin)


class OpenHoursAdmin(admin.ModelAdmin):
    list_display = ('vendor','from_hour','to_hour')
admin.site.register(OpeningHours,OpenHoursAdmin)
