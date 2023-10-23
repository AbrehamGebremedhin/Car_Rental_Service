from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    def rename_image(instance, filename):
        return f"static/driver_license/{instance.user}.jpg"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    driver_license = models.ImageField(upload_to=rename_image)
