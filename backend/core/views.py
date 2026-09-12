from rest_framework import generics
from .models import Service, GalleryItem, SiteSetting, BookingRequest
from .serializers import ServiceSerializer, GalleryItemSerializer, SiteSettingSerializer, BookingRequestSerializer

class ServiceList(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.filter(featured=True)

class GalleryList(generics.ListAPIView):
    serializer_class = GalleryItemSerializer
    queryset = GalleryItem.objects.all()

class SettingsView(generics.RetrieveAPIView):
    serializer_class = SiteSettingSerializer
    queryset = SiteSetting.objects.all()

    def get_object(self):
        obj = SiteSetting.objects.first()
        if not obj:
            obj = SiteSetting.objects.create()
        return obj

class BookingCreate(generics.CreateAPIView):
    serializer_class = BookingRequestSerializer
    queryset = BookingRequest.objects.all()
