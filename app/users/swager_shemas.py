from drf_yasg import openapi

get_list_of_users = {
    'operation_summary': "Get users list",
    'operation_description': "Return list of users filtered by username. Sample request: /users/?username=ko",
    "manual_parameters": [
        openapi.Parameter('username', openapi.IN_QUERY, description="Username", type=openapi.TYPE_STRING),
    ]
}