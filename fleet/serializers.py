from rest_framework.serializers import ModelSerializer
from fleet.models import Vehicle, Maintenance


class MaintenanceSerializer(ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'


class VehicleSerializer(ModelSerializer):
    maintenance = MaintenanceSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = [
            'VIN',
            'Brand',
            'Model',
            'Year',
            'Type',
            'License_plate',
            'milage',
            'fuel_consumption',
            'vehicle_picture',
            'maintenance',
            'created_on',
            'updated_on'
        ]
