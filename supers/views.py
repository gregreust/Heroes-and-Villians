from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers
from super_types.models import SuperType

# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == 'GET':

        super_param = request.query_params.get('super_type') 
        queryset = Supers.objects.all()

        if super_param:         #if parameter, filter
            queryset = queryset.filter(super_type__type = super_param)
            serializer = SupersSerializer(queryset, many=True)
            return Response(serializer.data)

        else:
            super_types = SuperType.objects.all()
            custom_response_dict = {}
            for type in super_types:
                supers = Supers.objects.filter(super_type=type.id)
                supers_serializer = SupersSerializer(supers, many=True)
                custom_response_dict[type.type] = {
                    'supers': supers_serializer.data
                }
           
            return Response(custom_response_dict)
    
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_by_id(request, pk):
    super = get_object_or_404(Supers, id = pk)
    if request.method == 'GET':
        serializer = SupersSerializer(super)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)

    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)