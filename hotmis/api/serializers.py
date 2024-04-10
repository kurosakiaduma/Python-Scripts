#returns values from the models in JSON format
from rest_framework import serializers
from .models import Room, Booking, Client

class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['r_id', 'rname', 'price_rate', 'size', 'available']
        
class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['c_id', 'c_fname', 'c_lname', 'gender']
        
class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['b_id','booking_date', 'r_id', 'c_id', 'st_dt', 'end_dt', 'total_price']