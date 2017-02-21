
from rest_framework import generics
from .serializers import BucketlistSerializer, ZgloszeniaSerializer
from .models import Bucketlist, Zgloszenie

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer



class CreateView_Zgloszenie(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Zgloszenie.objects.all()
    serializer_class  = ZgloszeniaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView_Zgloszenie(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Zgloszenie.objects.all()
    serializer_class = ZgloszeniaSerializer
