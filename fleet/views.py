from .models import Vehicle, Maintenance
from .serializers import VehicleSerializer, MaintenanceSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class VehicleList(APIView):
    """
    List all vehicles, or create a new vehicle.
    """
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleDetail(APIView):
    """
    Retrieve, update or delete a vehicle instance.
    """
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def put(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vehicle = self.get_object(pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MaintenanceList(APIView):
    """
    List all maintenances for a vehicle, or create a new maintenance for a vehicle.
    """
    #permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        maintenances = Maintenance.objects.filter(Vehicle_id=pk)
        serializer = MaintenanceSerializer(maintenances, many=True)
        print(pk)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = MaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MaintenanceDetail(APIView):
    """
    Retrieve, update or delete a Maintenance instance.
    """
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        maintenance = self.get_object(pk)
        serializer = MaintenanceSerializer(maintenance)
        return Response(serializer.data)

    def put(self, request, pk):
        maintenance = self.get_object(pk)
        serializer = MaintenanceSerializer(maintenance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        maintenance = self.get_object(pk)
        maintenance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
