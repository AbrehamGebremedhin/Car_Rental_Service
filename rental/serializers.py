from rest_framework.serializers import ModelSerializer
from rental.models import Rental, Reservation


class RentSerializer(ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
