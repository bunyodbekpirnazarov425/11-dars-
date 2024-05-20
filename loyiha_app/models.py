from django.db import models

class Airline(models.Model):
    air_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="country_image", null=True)
    text = models.TextField(max_length=2000, null=True)
    
    def __str__(self) -> str:
        return f"{self.air_name}"
    
class Country(models.Model):
    country = models.CharField(max_length=100)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name="country")
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="country_image", null=True)
    text = models.TextField(max_length=2000, null=True)
    
    def __str__(self) -> str:
        return f"{self.country}"
    
class States(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="country_image", null=True)
    text = models.TextField(max_length=2000, null=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
