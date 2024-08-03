from django.db import models


# Create your models here.

class Drone(models.Model):
    model = models.CharField(max_length=20)
    payload_capacity = models.PositiveIntegerField()
    unit = models.CharField(max_length=5, choices=(('grams', 'Grams'), ('kg', 'KiloGrams'),))
    battery_life = models.PositiveIntegerField()
    status = models.CharField(max_length=15,
                              choices=(
                                      ('available', 'Available'),
                                      ('on flight', 'On Flight'),
                                      ('out of service', 'Out of  Service'),
                                  )
                              )

    def __str__(self):
        return f"{self.model},  btry: {self.battery_life}, paylaod: {self.payload_capacity}"


class Flight(models.Model):
    order = models.ForeignKey('store.Order', on_delete=models.CASCADE, null=True, blank=True)
    drone = models.ForeignKey('Drone', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.drone}"