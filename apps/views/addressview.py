from rest_framework.views import APIView
from rest_framework.response import Response
from . import AddressSerializer
from . import AddressModel
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
import datetime

class AddressList(generics.GenericAPIView):
    serializer_class = AddressSerializer
    queryset = AddressModel.objects.all()
    """
    List all travel request list details
    """
    def get(self, request, format=None):
        serializer = AddressSerializer(self.get_queryset(), many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        """Reference of Valid Phone number formatting
            (This also depends on the value which user enter on the UI part)
            +(61) 455 562 400
            +61-455-562-400
            +61 455 562 400
            +(61)-455-562-400
            +(61) 455 562 400
            (02) 4371 3164
            (02) 4371-3164
            02 80268989
            03 80268989
            04 80268989
            05 80268989
            433245898
            433 245 898
            433-245-898
            4555-62400
            123456
            08 54 587 456
        """
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressDetail(APIView):
    """
    View or Delete a address instance.
    """
    def get(self, request, pk, format=None):
        address = get_object_or_404(AddressModel, pk=pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        address = get_object_or_404(AddressModel, pk=pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
