from drf_yasg import openapi
from rest_framework import status

from .serializers import InvitationSerializer

send_invitation_schema = {
    'operation_summary': "Send invitation",
    'operation_description': "Sends an invitation to a user to join a house. Check if user is already invited to this house.",
    'responses': {
        status.HTTP_201_CREATED: openapi.Response('Invitation Created'),
        status.HTTP_400_BAD_REQUEST: openapi.Response('Error', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))
            }
        ))
    }
}

get_invitation_schema = {
    'operation_summary': "Get invitation by id",
    'operation_description': "Returns an invitation."
}

solve_invitation_schema = {
    'operation_summary': "Solve invitation",
    'operation_description': "Accepts or declines an invitation with given id.",
    'responses': {
        status.HTTP_200_OK: openapi.Response(description='Successful Response', schema=InvitationSerializer),
        status.HTTP_400_BAD_REQUEST: openapi.Response('Error', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))
            }
        ))
    }
}
