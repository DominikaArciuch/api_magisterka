from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer, CreateTaskSerializer, BaseTaskSerializer
from .swagger_schemas import get_task_list_schema, create_task_schema, get_base_task_list_schema, \
    create_base_task_schema, get_task_details_list_schema, delete_task_schema, edit_task_schema


class CreateTaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTaskSerializer
        return TaskSerializer

    @swagger_auto_schema(**create_task_schema)
    def post(self, request, *args, **kwargs):
        data = self.get_serializer(data=request.data)
        if data.is_valid():
            if data.validated_data['assigned_users'] is None and data.validated_data['house'] is None:
                data.validated_data['assigned_users'] = self.request.user
            data.validated_data['created_by'] = self.request.user
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Task.objects.all()
        assigned_user_id = self.request.query_params.get('assigned_user')
        house_id = self.request.query_params.get('house')
        created_by_id = self.request.query_params.get('created_by')

        if assigned_user_id is not None:
            queryset = queryset.filter(assigned_users__id=assigned_user_id)
        if house_id is not None:
            queryset = queryset.filter(house__id=house_id)
        if created_by_id is not None:
            queryset = queryset.filter(created_by__id=created_by_id)

        return queryset

    @swagger_auto_schema(**get_task_list_schema)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**get_task_details_list_schema)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(method='put', auto_schema=None)
    @api_view(['PUT'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(**delete_task_schema)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(**edit_task_schema)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class BaseTasksView(generics.ListCreateAPIView):
    queryset = Task.objects.filter(is_base=True).all()
    serializer_class = BaseTaskSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdminUser()]
        else:
            return [IsAuthenticated()]

    @swagger_auto_schema(**get_base_task_list_schema)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(**create_base_task_schema)
    def post(self, request, *args, **kwargs):
        data = self.get_serializer(data=request.data)
        if data.is_valid():
            data.validated_data['is_base'] = True
            data.validated_data['created_by'] = self.request.user
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
