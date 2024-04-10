from django.db import models
import random

# Create your models here.
class Room(models.Model):
    r_id = models.CharField(max_length=2, default="", unique=True, primary_key=True, auto_created=True)
    
    class rm_choices(models.TextChoices):
        EVE = "Everest" 
        HIM =  "Himalayas" 
        RUS = "Rushmore"
        KIL = "Kilimanjaro" 
        KEN = "Kenya"
    class size_choices(models.TextChoices):
        Single = "Single (1)"
        Double = "Double (2)"
        Queen = "Queen (2+)"
    
    rname = models.CharField(max_length=16, choices=rm_choices.choices, default=rm_choices.EVE)
    price_rate = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.CharField(default=size_choices.Single, choices=size_choices.choices, max_length=10)
    available = models.BooleanField(default=True, null=False)
    
    def __str__(self) -> str:
        return f"{self.r_id} {self.rname} at {self.price_rate} per day"
    
class Client(models.Model):
    c_id = models.CharField(primary_key=True, null=False, max_length=6)
    c_fname = models.TextField(null=False)
    c_lname = models.TextField(null=False)
    
    class Gender(models.TextChoices):
        M = "Male"
        F = "Female"
        O = "Non-binary"
        
    gender = models.CharField(choices=Gender.choices, max_length=12)



class Booking(models.Model):
    b_id = models.IntegerField(primary_key=True, auto_created=True)    
    booking_date = models.DateTimeField(auto_now_add=True)
    r_id = models.ForeignKey(Room, on_delete=models.CASCADE, editable=False)
    c_id = models.ForeignKey(Client, on_delete=models.CASCADE, editable=False)
    st_dt = models.DateField(null=False)
    end_dt = models.DateField(null=False)
    total_price = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    
    def __str__(self) -> str:
        return f"Booking {self.b_id} for {Room.rname} made by {Client.c_fname} {Client.c_lname} for the period between {self.st_dt} till {self.end_dt}"
    