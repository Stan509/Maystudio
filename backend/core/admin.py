from django.contrib import admin
from .models import Service, GalleryItem, SiteSetting, BookingRequest

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'featured', 'sort_order')
    list_editable = ('featured', 'sort_order')
    search_fields = ('name_en', 'name_fr')

@admin.register(GalleryItem)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'sort_order')
    list_editable = ('category', 'sort_order')

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address', 'special_price', 'home_service')

@admin.register(BookingRequest)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'preferred_date', 'preferred_time', 'home_service', 'status')
    list_filter = ('status', 'home_service', 'preferred_date')
    search_fields = ('name', 'phone', 'email')
