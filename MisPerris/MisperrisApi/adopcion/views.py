from rest_framework import generics
from .models import Dog
from .serializers import DogSerializer
from django.shortcuts import get_object_or_404

class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    
    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

        