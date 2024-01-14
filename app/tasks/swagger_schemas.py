from drf_yasg import openapi
from rest_framework import status

from .serializers import TaskSerializer

create_task_schema = {
    'operation_summary': "Create task",
    'responses': {
        status.HTTP_201_CREATED: openapi.Response(description='Task created', schema=TaskSerializer),
        status.HTTP_400_BAD_REQUEST: openapi.Response('Error', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))
            }
        ))
    }
}

get_task_list_schema = {
    'operation_summary': "Get tasks",
    'operation_description': "You can filter tasks by assigned_user, house and created_by. Sample request: /tasks/?assigned_user=1&house=2&created_by=3",
    "manual_parameters": [
        openapi.Parameter('assigned_user', openapi.IN_QUERY, description="ID of the assigned user",
                          type=openapi.TYPE_INTEGER),
        openapi.Parameter('house', openapi.IN_QUERY, description="ID of the house", type=openapi.TYPE_STRING),
        openapi.Parameter('created_by', openapi.IN_QUERY, description="ID of the user who created the task",
                          type=openapi.TYPE_INTEGER)
    ]
}

get_base_task_list_schema = {
    'operation_summary': "Get base tasks",
    'operation_description': "Return list of predefined tasks.",
}

get_task_details_list_schema = {
    'operation_summary': "Get task by id",
    'operation_description': "Return information about task.",
}

create_base_task_schema = {
    'operation_summary': "Create base task, only for admin",
    'responses': {
        status.HTTP_201_CREATED: openapi.Response(description='Task created', schema=TaskSerializer),
        status.HTTP_400_BAD_REQUEST: openapi.Response('Error', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))
            }
        )),
        status.HTTP_403_FORBIDDEN: openapi.Response('Error', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))
            }
        ))
    }
}

edit_task_schema = {
    'operation_summary': "Edit task",
    'responses': {
        status.HTTP_200_OK: openapi.Response(description='Task edited', schema=TaskSerializer),
        status.HTTP_400_BAD_REQUEST: openapi.Response('Error', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))
            }
        ))
    }
}

delete_task_schema = {
    'operation_summary': "Delete task",
}
