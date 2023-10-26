from django.db import models


# Create your models here.
# noinspection PyMethodParameters
class Vehicle(models.Model):
    def rename_image(instance, filename):
        return f"static/car_images/{instance.License_plate}.jpg"
    SEDAN = "SEDAN"
    COUPE = "COUPE"
    SPORTS = "SPORTS"
    STATIONWAGON = "STATIONWAGON"
    HATCHBACK = "HATCHBACK"
    CONVERTIBLE = "CONVERTIBLE"
    SUV = "SUV"
    MINIVAN = "MINIVAN"
    PICKUP = "PICKUP"
    VEHICLE_CHOICES = [
        (SEDAN, "Sedan"),
        (COUPE, "Coupe"),
        (SPORTS, "Sports"),
        (STATIONWAGON, "StationWagon"),
        (HATCHBACK, "HatchBack"),
        (CONVERTIBLE, "Convertible"),
        (SUV, "SUV"),
        (MINIVAN, "MiniVan"),
        (PICKUP, "PickUp Truck"),
    ]
    VIN = models.CharField(max_length=50, unique=True)
    Brand = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Year = models.DateField()
    Type = models.CharField(max_length=20, choices=VEHICLE_CHOICES, default=SEDAN)
    License_plate = models.CharField(max_length=7, unique=True)
    milage = models.FloatField()
    fuel_type = models.CharField(max_length=50, default="Diesel")
    fuel_consumption = models.FloatField()
    vehicle_picture = models.ImageField(null=True, upload_to=rename_image)
    is_available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Type} - {self.Brand} {self.Model} - {self.License_plate}"


class Maintenance(models.Model):
    repair_done_on = models.DateField(auto_now_add=True)
    repairs = models.TextField()
    next_repair = models.FloatField()
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenance')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Vehicle} - {self.updated_on}"
