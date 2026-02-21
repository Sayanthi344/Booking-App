from django.db import models

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
    captions = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.room.name} - {self.captions or 'no caption'}"