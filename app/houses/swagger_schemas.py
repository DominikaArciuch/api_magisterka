from drf_yasg import openapi
from rest_framework import status

from .serializers import HouseSerializer, ListHousesSerializer, CreateHouseSerializer

get_house_schema = {
    'operation_summary': "Get house by id",
}

get_house_list_schema = {
    'operation_summary': "Get houses",
    'responses': {
        status.HTTP_200_OK: openapi.Response(description='House list', schema=ListHousesSerializer),
        status.HTTP_400_BAD_REQUEST: openapi.Response('Error', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))
            }
        ))
    }
}

delete_house_schema = {
    'operation_summary': "Delete house",
}

edit_house_schema = {
    'operation_summary': "Edit house",
    'responses': {
        status.HTTP_200_OK: openapi.Response(description='House edited', schema=HouseSerializer),
        status.HTTP_400_BAD_REQUEST: openapi.Response('Error', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))
            }
        ))
    }
}

create_house_schema = {
    'operation_summary': "Create house",
    'responses': {
        status.HTTP_201_CREATED: openapi.Response(description='House created', schema=CreateHouseSerializer),
        status.HTTP_400_BAD_REQUEST: openapi.Response('Error', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))
            }
        ))
    }
}
