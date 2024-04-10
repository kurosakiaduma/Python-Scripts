from django.urls import path, include
from api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'rooms', RoomView, basename='rooms')
router.register(r'clients', ClientView, basename='clients')
router.register(r'bookings', BookingView, basename='bookings')


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'available-rooms', AvailableRooms.as_view())
]

