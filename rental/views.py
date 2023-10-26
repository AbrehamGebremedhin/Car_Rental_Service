from .models import Rental, Reservation
from fleet.models import Vehicle
from fleet.serializers import VehicleSerializer
from .serializers import RentSerializer, ReservationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated


class RentList(APIView):
    """
    List all rentals, or create a new rental.
    """

    # permission_classes = [IsAuthenticated]
    @staticmethod
    def get_object(pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    @staticmethod
    def get():
        rents = Rental.objects.all()
        serializer = RentSerializer(rents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RentSerializer(data=request.data)
        vehicle = self.get_object(request.data['vehicle'])

        vehicle_serializer = VehicleSerializer(vehicle, data={"is_available": False}, partial=True)

        if serializer.is_valid():
            if vehicle_serializer.is_valid():
                vehicle_serializer.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentDetail(APIView):
    """
    Retrieve, update or delete a vehicle instance.
    """

    # permission_classes = [IsAuthenticated]

    @staticmethod
    def get_object(pk):
        try:
            return Rental.objects.get(pk=pk)
        except Rental.DoesNotExist:
            raise Http404

    @staticmethod
    def get_vehicle_object(pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, pk):
        rental = self.get_object(pk)
        serializer = RentSerializer(rental)
        return Response(serializer.data)

    def put(self, request, pk):
        rental = self.get_object(pk)
        serializer = RentSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        # Retrieve the object to be updated
        obj = self.get_object(pk)
        rent = RentSerializer(obj)
        vehicle = self.get_vehicle_object(rent.data['vehicle'])
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not vehicle:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Updates the car availability status of the given vehicle
        if request.data['status'] == 'RENTED' or request.data['status'] == 'RESERVED':
            vehicle_serializer = VehicleSerializer(vehicle, data={'is_available': False}, partial=True)
            if vehicle_serializer.is_valid():
                vehicle_serializer.save()
        else:
            vehicle_serializer = VehicleSerializer(vehicle, data={'is_available': True}, partial=True)
            if vehicle_serializer.is_valid():
                vehicle_serializer.save()

        # Apply the partial update
        serializer = RentSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        rental = self.get_object(pk)
        rental = RentSerializer(rental)
        vehicle = self.get_vehicle_object(rental.data['vehicle'])
        vehicle_serializer = VehicleSerializer(vehicle, data={'is_available': True}, partial=True)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()

        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReservationList(APIView):
    """
    List all rentals, or create a new rental.
    """

    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self):
        reserves = Reservation.objects.all()
        serializer = ReservationSerializer(reserves, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        vehicle = self.get_object(request.data['vehicle'])

        vehicle_serializer = VehicleSerializer(vehicle, data={'is_available': False}, partial=True)

        if serializer.is_valid():
            if vehicle_serializer.is_valid():
                vehicle_serializer.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationDetail(APIView):
    """
    Retrieve, update or delete a reservation instance.
    """

    # permission_classes = [IsAuthenticated]

    @staticmethod
    def get_object(pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404

    @staticmethod
    def get_vehicle_object(pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, pk):
        reservation = self.get_object(pk)
        serializer = RentSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        # Retrieve the object to be updated
        obj = self.get_object(pk)
        reservation = ReservationSerializer(obj)
        vehicle = self.get_vehicle_object(reservation.data['car'])

        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not vehicle:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Apply the partial update
        serializer = RentSerializer(obj, data=request.data, partial=True)
        vehicle_serializer = VehicleSerializer(vehicle, data={'is_available': False}, partial=True)

        if serializer.is_valid():
            if vehicle_serializer.is_valid():
                vehicle_serializer.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        reservation = self.get_object(pk)
        reservation = ReservationSerializer(reservation)
        vehicle = self.get_vehicle_object(reservation.data['car'])
        vehicle_serializer = VehicleSerializer(vehicle, data={'is_available': True}, partial=True)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
