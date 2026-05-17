from django.contrib import admin
from .models import Room,RoomImages,OccupiedDate
# Register your models here.

admin.site.register(Room)
admin.site.register(RoomImages)
admin.site.register(OccupiedDate)

