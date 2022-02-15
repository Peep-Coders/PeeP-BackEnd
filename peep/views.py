# Create your views here.
from rest_framework import generics
from .models import Peep, Chirp
from .serializers import PeepSerializer, ChirpSerializer
from rest_framework import permissions
from peep.permissions import IsOwnerOrReadOnly

# Create your views here.

class PeepList(generics.ListCreateAPIView):
    queryset = Peep.objects.all()
    serializer_class = PeepSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PeepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Peep.objects.all()
    serializer_class = PeepSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ChirpList(generics.ListCreateAPIView):
    queryset = Chirp.objects.all()
    serializer_class = ChirpSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChirpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chirp.objects.all()
    serializer_class = ChirpSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
