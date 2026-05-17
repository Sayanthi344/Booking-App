from rest_framework import serializers
from .models import Room,RoomImages,OccupiedDate,User

class RoomImageSerializer(serializers.HyperlinkedModelSerializer):
    room =serializers.HyperlinkedRelatedField(
        view_name='room-detail', queryset=Room.objects.all()),
    class Meta:
        model = RoomImages
        fields = [ 'id', 'image', 'captions','room']

class OccupiedDateSerializer(serializers.HyperlinkedModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name='room-detail',
        queryset=Room.objects.all())
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all())
    class Meta:
        model = OccupiedDate
        fields = ['url','id', 'room', 'date','user']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)
    occupiedDates = OccupiedDateSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['url','id', 'name', 'type', 'currency', 'maxOccupancy', 'description']

from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url','id', 'username', 'email', 'full_name', 'password']

    def validate_password(self, value):
        return make_password(value  )