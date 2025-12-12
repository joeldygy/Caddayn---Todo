from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core_app.models import (
    get_all_todos, create_todo, get_todo,
    update_todo, delete_todo
)
from core_app.serializer.todo_request import (
    TodoCreateRequestSerializer,
    TodoUpdateRequestSerializer
)
from core_app.serializer.todo_response import TodoResponseSerializer


class TodoController:

    @staticmethod
    @api_view(['GET'])
    def list(request):
        todos = get_all_todos()
        serializer = TodoResponseSerializer(todos, many=True)
        return Response(serializer.data)

    @staticmethod
    @api_view(['POST'])
    def create(request):
        todo = create_todo(request.data)
        serializer = TodoCreateRequestSerializer(todo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    @api_view(['GET'])
    def detail(request, id):
        todo = get_todo(id)
        serializer = TodoResponseSerializer(todo)
        return Response(serializer.data)

    @staticmethod
    @api_view(['PUT'])
    def update(request, id):
        todo = update_todo(id, request.data)
        serializer = TodoUpdateRequestSerializer(todo)
        return Response(serializer.data)

    @staticmethod
    @api_view(['DELETE'])
    def delete(request, id):
        delete_todo(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
