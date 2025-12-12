from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core_app.models import (
    get_all_todos, create_todo, get_todo,
    update_todo, delete_todo
)
from core_app.serializer.todo_request import TodoCreateRequestSerializer
from core_app.serializer.todo_request import TodoUpdateRequestSerializer


@api_view(['GET'])
def todo_list(request):
    todos = get_all_todos()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todo_create(request):
    todo = create_todo(request.data)
    serializer = TodoCreateRequestSerializer(todo)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def todo_detail(request, id):
    todo = get_todo(id)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)


@api_view(['PUT'])
def todo_update(request, id):
    todo = update_todo(id, request.data)
    serializer = TodoUpdateRequestSerializer(todo)
    return Response(serializer.data)


@api_view(['DELETE'])
def todo_delete(request, id):
    delete_todo(id)
    return Response(status=status.HTTP_204_NO_CONTENT)



