import datetime
import statistics

from .models import (
    WindReading
)


def daily_average(obj)-> float | str:
    """
    Get the wind readings of the current day and
    Calculate the mean.
    """
    today =  datetime.datetime.today()
    readings = []
    for reading in WindReading.objects.filter(anemometer=obj, date=today):
        readings.append(reading.wind_speed)
    if readings : 
        avg = statistics.mean(readings)   
        return round(avg, 2)       
    return f"No reading yet for {obj} today"


def weekly_average(obj) -> float | str:
    """
    Get the wind readings of the current week and
    Calculate the mean.
    """
    today =  datetime.datetime.today()
    start_week = today - datetime.timedelta(today.weekday())
    end_week = start_week + datetime.timedelta(7)
    readings = []
    for reading in WindReading.objects.filter(
        anemometer=obj,
        date__range=[start_week, end_week]
    ):
        readings.append(reading.wind_speed)
    if readings : 
        avg = statistics.mean(readings)   
        return round(avg, 2)      
    return f"No reading yet for {obj} this week"