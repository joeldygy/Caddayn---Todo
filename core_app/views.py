from rest_framework.response import Response
from rest_framework import status

from core_app.models import (
    get_all_todos,
    create_todo,
    get_todo,
    update_todo,
    delete_todo
)

from core_app.serializer.todo_request import (
    TodoCreateRequestSerializer,
    TodoUpdateRequestSerializer
)

from core_app.serializer.todo_response import TodoResponseSerializer
from core_app.utils import TodoUtils


class TodoView:

    def todo_list(self, request):
        todos = get_all_todos()
        serializer = TodoResponseSerializer(todos, many=True)

        # map using utils
        mapped = TodoUtils().mapper(serializer.data)

        return Response(
            data={"message": "Todos fetched successfully", "data": mapped},
            status=status.HTTP_200_OK
        )

    def todo_create(self, request):
        serializer = TodoCreateRequestSerializer(data=request.data)

        if serializer.is_valid():
            dto = serializer.to_dto()
            todo = create_todo(dto.__dict__)

            return Response(
                data={
                    "message": "Todo created successfully",
                    "data": TodoResponseSerializer(todo).data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def todo_detail(self, request, id):
        try:
            todo = get_todo(id)
        except Exception:  # You can replace Exception with specific DoesNotExist if using Django ORM
            return Response(
                {"message": "Todo not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoResponseSerializer(todo)
        return Response(
            data={"message": "Todo fetched successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def todo_update(self, request, id):
        try:
            existing = get_todo(id)
        except Exception:
            return Response(
                {"message": "Todo not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoUpdateRequestSerializer(data=request.data)

        if serializer.is_valid():
            dto = serializer.to_dto(existing)
            updated = update_todo(id, dto.__dict__)

            return Response(
                data={
                    "message": "Todo updated successfully",
                    "data": TodoResponseSerializer(updated).data
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def todo_delete(self, request, id):
        try:
            delete_todo(id)
        except Exception:
            return Response(
                {"message": "Todo not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {"message": "Todo deleted successfully"},
            status=status.HTTP_200_OK
        )
