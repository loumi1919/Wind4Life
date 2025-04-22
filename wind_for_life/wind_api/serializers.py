from rest_framework.response import Response
from rest_framework import serializers

from .models import (
    Anemometer, 
    WindReading
)

from .utils import weekly_average, daily_average



class AnemometerSerializer(serializers.ModelSerializer[Anemometer]):
    class Meta:
        model = Anemometer
        fields = "__all__"
        examples = [
            {
                "id" : 1,
                "name": "Paris",
                "long" : 2.333333,
                "lat" : 48.866667,
            }
        ]


class WindReadingCreateSerializer(serializers.ModelSerializer[WindReading]):
    """
    Wind reading submission
    """
    class Meta:
        model = WindReading
        fields = "__all__"
        examples = [
            {
                "wind_speed": 55.0,
                "wind_unit" : "Knots",
                "anemometer" : "Dakar",
            }
        ]
        

class AnemometerReadingsSerializer(
    serializers.ModelSerializer[Anemometer]
):
    """
    Anemometer List with their last 5 ratings
    """
    wind_readings = serializers.SerializerMethodField()
    daily_average = serializers.SerializerMethodField()
    weekly_average = serializers.SerializerMethodField()
    
    class Meta:
        model = Anemometer
        fields = [
            "name", 
            "wind_readings", 
            "daily_average", 
            "weekly_average"
        ] 
        examples = [
            {
                "name" : "Paris",
                "wind_readings" : [18, 22, 45, 21, 13],
                "daily_average" : 16.23,
                "weekly_average" : 19.10,             
            }
        ]
        
    def get_wind_readings(self, obj):
        readings = []
        for reading in WindReading.objects.filter(anemometer=obj):
            readings.append(reading.wind_speed)     
        return readings[-5:]
    
    def get_daily_average(self, obj):
        return daily_average(obj)
            
    def get_weekly_average(self, obj):
        return weekly_average(obj)
        

        
    
class AnemometerReadingsAverageSerializer(
    serializers.ModelSerializer[Anemometer]
):
    """
    Daily/Weekly mean wind speed for Anemometer
    """
    daily_average = serializers.SerializerMethodField()
    weekly_average = serializers.SerializerMethodField()
    
    class Meta:
        model = Anemometer
        fields =  ["name", "daily_average", "weekly_average"] 
        examples = [
            {
                "name" : "Paris",
                "daily_average" : 22,
                "weekly_average" : 19.5,
            }
        ]
    
    def get_daily_average(self, obj):
        return daily_average(obj)
            
    def get_weekly_average(self, obj):
        return weekly_average(obj)
    
  
        

class AnemometerReadingsListSerializer(
    serializers.ModelSerializer[WindReading]
):
    """
    Daily/Weekly mean wind speed for Anemometer
    """
    anemometer = serializers.StringRelatedField()
    class Meta:
        model = WindReading
        fields =  ["anemometer", "wind_speed", "wind_unit", "date"]
        examples = [
            {
                "anemometer" : "Paris",
                "wind_speed" : 22.00,
                "wind_unit" : "knots",
                "date" : "2025-04-21"
            }
        ]
        



        


    