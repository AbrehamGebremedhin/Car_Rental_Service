from django.db import models
from accounts.models import Customer
from fleet.models import Vehicle


# Create your models here.
class Review(models.Model):
    rating = models.IntegerField(default=0)
    review = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, related_name='vehicle')

    def __str__(self):
        return f"{self.rating}"
