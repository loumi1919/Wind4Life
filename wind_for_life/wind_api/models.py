from django.db import models
from simple_history.models import HistoricalRecords
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


class Anemometer(models.Model): 
    """
    Anemomter model class
    """   
    class Meta:
        verbose_name = 'Anemomètre'
        unique_together = ['long', 'lat']
    
    name = models.CharField(
        max_length=255, 
        help_text= "The name of the Anemometer",
        unique=True
    )
    long = models.DecimalField(
        max_digits=9, 
        decimal_places=6,
        help_text= "The longitude coordinates",
        null=False,
        validators=[MinValueValidator(Decimal('-180.0')),
                    MaxValueValidator(Decimal('180.0'))]
    )
    lat = models.DecimalField(
        max_digits=9, 
        decimal_places=6,
        help_text="The latitude coordinates",
        null=False,
        validators=[MinValueValidator(Decimal('-90.0')),
                    MaxValueValidator(Decimal('90.0'))]
    )
    
    history = HistoricalRecords()
    
    def __str__(self) -> str:
        return self.name
    
 
    
class WindReading(models.Model):
    """
    WindReading model class
    """  
    
    class Meta:
        verbose_name = 'Mesure de vitesse du vent'
        unique_together = ['wind_speed', 'date', 'anemometer']
        
    class WindUnit(models.TextChoices):
        KNOTS = 'Knots' 
    
    anemometer = models.ForeignKey(
        Anemometer,
        on_delete=models.CASCADE,
        help_text="The given Anemometer",
        related_name="wind_readings"
    )
    
    wind_speed = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01')), 
                    MaxValueValidator(Decimal('200.00'))],
        verbose_name='vitesse (en nœuds)'
    )
    wind_unit = models.CharField(
        max_length=15,
        choices=WindUnit.choices, default=WindUnit.KNOTS
    )
    date = models.DateField()
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self) -> str: 
        return f'{self.anemometer.name} [{self.date}] - {self.wind_speed} {self.wind_unit}'
    


class Tags(models.Model):
    """
    Tags model class
    """ 
    class Meta:
        verbose_name = 'Tag'
        
    name = models.CharField(
        max_length=255, 
        help_text= "The name of the Tag",
        unique=True
    )
    wind_readings = models.ManyToManyField(
        WindReading,
        related_name="tags"
    )
    
    def __str__(self) -> str:
        return self.name