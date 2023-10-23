from django.db import models
from accounts.models import Customer
from fleet.models import Vehicle


# Create your models here.
class Rental(models.Model):
    pickup_date = models.DateField()
    return_date = models.DateField()
    confirmed = "CONFIRMED"
    on_rent = "RENTED"
    returned = "RETURNED"
    cancelled = "CANCELLED"
    reserved = "RESERVED"
    past_due = "PAST DUE"
    STATUS_CHOICES = [
        (confirmed, "Confirmed"),
        (on_rent, "Rented"),
        (returned, "Returned"),
        (cancelled, "Cancelled"),
        (reserved, "Reserved"),
        (past_due, "Past Due")
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=confirmed)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicle")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle} - {self.customer} -- {self.status}"
