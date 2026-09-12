from rest_framework import serializers
from .models import Service, GalleryItem, SiteSetting, BookingRequest

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = '__all__'

class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = '__all__'

class BookingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingRequest
        fields = ['id', 'name', 'phone', 'email', 'service', 'preferred_date', 'preferred_time', 'notes', 'home_service', 'status', 'created_at']
        read_only_fields = ['id', 'status', 'created_at']
