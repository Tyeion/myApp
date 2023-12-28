from django.db import models

# Create your models here.
class Passenger(models.Model):
    firstName = models.CharField(primary_key=True, max_length=30)
    lastName = models.CharField(max_length=20)
    travelPoints = models.IntegerField()

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.travelPoints}"
