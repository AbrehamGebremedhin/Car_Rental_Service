from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    def rename_image(instance, filename):
        return f"static/driver_license/{instance.user}.jpg"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    driver_license = models.ImageField(upload_to=rename_image)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete(*args, **kwargs)
