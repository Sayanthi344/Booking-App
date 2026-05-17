from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class Room(models.Model):
    ROOM_TYPES = [
      ('suite', 'Suite'),
      ('deluxe', 'Deluxe Room'),
      ('standard', 'Standard Room'),
    ]
    CURRENCY_TYPES = [
         ('USD', 'US Dollar'),
         ('EUR', 'Euro'),
         ('GBP', 'British Pound'),
      ]
    name = models.CharField(max_length=100,blank=True,default="")
    type = models.CharField(max_length=100, choices=ROOM_TYPES)
    pricePerNight = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(default="USD", max_length=10, choices=CURRENCY_TYPES)
    maxOccupancy = models.IntegerField(default=1)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name} ({self.type})"
    
class RoomImages(models.Model):
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')
    captions = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return f"Image for {self.room.name} - {self.captions or 'no caption'}"

class OccupiedDate(models.Model):
    room = models.ForeignKey(Room, related_name='occupied_dates', on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='booked_dates', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room.name} occupied on {self.date} by {self.user.full_name}"

class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, default="")

    