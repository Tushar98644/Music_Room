from django.shortcuts import render
# from django.http import HttpResponse as Httprs
from rest_framework import generics
from .serializers import RoomSerializer,CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView,Response,status
# Create your views here.

class Roomview(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class CreateRoomview(APIView):
    serializer_class = CreateRoomSerializer

    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            post_guest_can_pause = serializer.data.get('guest_can_pause')
            post_votes_to_skip = serializer.data.get('votes_to_skip')
            post_host = self.request.session.session_key
            queryset = Room.objects.filter(host=post_host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = post_guest_can_pause
                room.votes_to_skip = post_votes_to_skip
                room.save(update_fields=['guest_can_pause','votes_to_skip'])
                return Response(RoomSerializer(room).data,status=status.HTTP_200_OK)
            else:
                room = Room(host=post_host,guest_can_pause=post_guest_can_pause,votes_to_skip=post_votes_to_skip)
                room.save()
                return Response(RoomSerializer(room).data,status=status.HTTP_201_CREATED)
        return Response({'Bad Request':'Invalid Data...'},status=status.HTTP_400_BAD_REQUEST)
    
