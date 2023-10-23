from .models import Rental
from .serializers import RentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class RentList(APIView):
    """
    List all vehicles, or create a new vehicle.
    """
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        rents = Rental.objects.all()
        serializer = RentSerializer(rents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentDetail(APIView):
    """
    Retrieve, update or delete a vehicle instance.
    """
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Rental.objects.get(pk=pk)
        except Rental.DoesNotExist:
            raise Http404

    def get(self, request, pk):
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
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Apply the partial update
        print(request.data)
        serializer = RentSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rental = self.get_object(pk)
        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
