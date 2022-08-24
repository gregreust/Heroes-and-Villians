from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SuperTypeSerializer
from .models import SuperType


# Create your views here.
@api_view(['GET', 'POST'])
def type_list(request):
    
    if request.method == 'GET':

        queryset = SuperType.objects.all()
        serializer = SuperTypeSerializer(queryset, many=True)
        return Response(serializer.data)
  
    
    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def type_by_id(request, pk):

    type = get_object_or_404(SuperType, id = pk)

    if request.method == 'GET':
        serializer = SuperTypeSerializer(type)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(type, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)

    elif request.method == 'DELETE':
        type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)