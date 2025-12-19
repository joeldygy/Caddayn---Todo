from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from core_app.common.utils import CommonUtils
from core_app.todo.models import (
    get_all_todos,
    create_todo,
    get_todo,
    update_todo,
    delete_todo
)
from core_app.todo.utils import TodoUtils
from core_app.todo.serializer.todo_response import TodoResponseSerializer


class TodoView:

    def __init__(self):
        self.data_created = "Todo created successfully"
        self.data_fetched = "Todo fetched successfully"
        self.data_updated = "Todo updated successfully"
        self.data_deleted = "Todo deleted successfully"
        self.data_not_found = "Todo not found"

        super().__init__()


    def create_extract(self, params, token_payload=None):
        with transaction.atomic():
            create_todo(params.__dict__)

        return Response(
            status=status.HTTP_201_CREATED,
            data=CommonUtils.success_response_data(
                message=self.data_created
            )
        )


    def get_all_extract(self, params=None, token_payload=None):
        todos = get_all_todos()
        serializer = TodoResponseSerializer(todos, many=True)

        mapped = TodoUtils().mapper(serializer.data)

        return Response(
            status=status.HTTP_200_OK,
            data=CommonUtils.success_response_data(
                message=self.data_fetched,
                data=mapped
            )
        )


    def get_extract(self, params, token_payload=None):
        todo = get_todo(params.id)
        if not todo:
            raise ValueError(self.data_not_found)

        serializer = TodoResponseSerializer(todo)

        return Response(
            status=status.HTTP_200_OK,
            data=CommonUtils.success_response_data(
                message=self.data_fetched,
                data=serializer.data
            )
        )

    def update_extract(self, params, token_payload=None):
        todo = get_todo(params.id)
        if not todo:
            raise ValueError(self.data_not_found)

        with transaction.atomic():
            updated = update_todo(params.id, params.__dict__)

        serializer = TodoResponseSerializer(updated)

        return Response(
            status=status.HTTP_200_OK,
            data=CommonUtils.success_response_data(
                message=self.data_updated,
                data=serializer.data
            )
        )


    def delete_extract(self, params, token_payload=None):
        todo = get_todo(params.id)
        if not todo:
            raise ValueError(self.data_not_found)

        with transaction.atomic():
            delete_todo(params.id)

        return Response(
            status=status.HTTP_200_OK,
            data=CommonUtils.success_response_data(
                message=self.data_deleted
            )
        )
