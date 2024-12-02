from django.db import models

class Taxi(models.Model):
    name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=10)
    driver_name = models.CharField(max_length=100)
    passenger_capacity = models.IntegerField()
    car_model = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

