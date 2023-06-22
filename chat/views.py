from rest_framework import generics

from chat.models import Message, Group
from chat.serializers import GroupSerializer, MessageSerializer


class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class GroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = Group.objetcs.all()
    serializer_class = GroupSerializer


class GroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objetcs.all()
    serializer_class = GroupSerializer
