from django.contrib.auth.models import User


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


from .models import Anemometer, WindReading
from .serializers import (
    AnemometerSerializer, 
    WindReadingCreateSerializer,
    AnemometerReadingsSerializer,
    AnemometerReadingsAverageSerializer,
    AnemometerReadingsListSerializer
)



class ListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    


class AnemometerListCreateView(generics.ListCreateAPIView[Anemometer]):
    """
    Anemometer List View.
    Get all Anemometers and Create one. 
    """
    queryset = Anemometer.objects.all()
    serializer_class = AnemometerSerializer
    pagination_class = ListPagination
    permission_classes = [IsAuthenticated]


class AnemometerDetailView(generics.RetrieveUpdateDestroyAPIView[Anemometer]):
    """
    Anemometer Detail View. 
    Get/Edit/Delete an Anemometer.
    """
    queryset = Anemometer.objects.all()
    serializer_class = AnemometerSerializer

    lookup_field = 'name'
    


class WindReadingCreateView(generics.CreateAPIView[WindReading]):
    """
    Submit wind readings for an Anemometer.
    """
    queryset = WindReading.objects.all()
    serializer_class = WindReadingCreateSerializer
    permission_classes = [IsAuthenticated]



class AnemometerReadingsListView(generics.ListAPIView):
    """
    Anemometer List with their 5 last wind reading.
    Their daily and wikly wind readings means.
    """
    queryset = Anemometer.objects.all()
    serializer_class = AnemometerReadingsSerializer
    pagination_class = ListPagination


    
    
class AnemometerReadingsAverageView(generics.RetrieveAPIView):
    """
    Get daily and wikly wind readings means for an Anemometer.
    """
    queryset = Anemometer.objects.all()
    serializer_class = AnemometerReadingsAverageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'name'
    


class AnemometerAllReadingsListView(generics.ListAPIView):
    """
    Get all paginated wind readings for an Anemometer.
    """
    queryset = WindReading.objects.all()
    serializer_class = AnemometerReadingsListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tags']
    pagination_class = ListPagination
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        if (id := self.kwargs.get("id", None)) is None:
            # The Id field must always be filled
            raise Exception("The id must be filled")
        else :             
            return WindReading.objects.filter(anemometer=id)



    
    



    
    

