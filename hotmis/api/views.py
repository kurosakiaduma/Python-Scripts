from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from django.shortcuts import render
from .serializers import roomSerializer,clientSerializer, bookingSerializer
from .models import Room, Client, Booking
import requests


# Create your views here.
class RoomView(viewsets.ModelViewSet):
    queryset =  Room.objects.all()
    serializer_class = roomSerializer
    
class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    
class ClientView(viewsets.ViewSet):
    queryset =  Client.objects.all()
    serializer = clientSerializer
    
class AvailableRooms(APIView):
    def get(self, request, st_dt, end_dt):
        booked_rooms = Booking.objects.filter(Q(st_dt__range=[st_dt, end_dt]) | Q(end_dt__range=[st_dt, end_dt])).values_list('r_id', flat=True)
        available_rooms = Room.objects.filter(~Q(r_id__in=booked_rooms), available=True)
        serializer = roomSerializer(available_rooms, many=True)
        return Response(serializer.data)
    
def availableRooms(request):
    response =  requests.get('http://127.0.0.1:8000/apis/available-rooms')