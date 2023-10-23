from rest_framework.serializers import ModelSerializer
from accounts.serializers import CustomerSerializer
from fleet.serializers import VehicleSerializer
from rental.models import Rental


class RentSerializer(ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'
