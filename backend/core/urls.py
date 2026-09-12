from django.urls import path
from .views import ServiceList, GalleryList, SettingsView, BookingCreate

urlpatterns = [
    path('services/', ServiceList.as_view()),
    path('gallery/', GalleryList.as_view()),
    path('settings/', SettingsView.as_view()),
    path('bookings/', BookingCreate.as_view()),
]
