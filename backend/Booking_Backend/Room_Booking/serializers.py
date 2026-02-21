from rest_framework import serializers
from .models import Room,RoomImages

class RoomImageSerializer(serializers.HyperlinkedModelSerializer):
    room =serializers.HyperlinkedRelatedField(
        view_name='room-detail', queryset=Room.objects.all()),
    class Meta:
        model = RoomImages
        fields = [ 'id', 'image', 'captions','room']

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['url','id', 'name', 'type', 'currency', 'maxOccupancy', 'description']