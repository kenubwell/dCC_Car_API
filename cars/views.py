# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car
from cars import serializers


@api_view(['GET', 'POST'])
def cars_list(request):
    
    if request.method == 'GET':
        cars = Car.objects.all()
        serializers = CarSerializer(cars, many=True) #this is going to take our car table and convert to json
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = CarSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)  #this validates that API user input is true or accurate to the database
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

