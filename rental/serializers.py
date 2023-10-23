from rest_framework.serializers import ModelSerializer
from accounts.serializers import CustomerSerializer
from fleet.serializers import VehicleSerializer
from rental.models import Rental


class RentSerializer(ModelSerializer):
    vehicle = VehicleSerializer(many=True, read_only=True)
    customer = CustomerSerializer(many=True, read_only=True)

    class Meta:
        model = Rental
        fields = [
            'vehicle',
            'customer',
            'pickup_date',
            'return_date',
            'status',
            'created_on',
            'updated_on'
        ]
