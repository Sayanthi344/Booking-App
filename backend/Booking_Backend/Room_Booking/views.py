from django.shortcuts import render
from django.urls import reverse
from rest_framework import generics
from .models import Room
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RoomSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'rooms': reverse('room-list', request=request, format=format)
    })

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer 

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]