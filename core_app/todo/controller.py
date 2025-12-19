from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from core_app.todo.views import TodoView
from core_app.todo.serializer.todo_request import TodoCreateRequestSerializer
from core_app.todo.serializer.todo_request import TodoUpdateRequestSerializer
from core_app.todo.serializer.todo_response import TodoResponseSerializer
from core_app.common.utils import CommonUtils


class TodoController:


    @api_view(['POST'])
    def create(request: Request) -> Response:
        serializer = TodoCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return TodoView().create_extract(
            params=params,
            token_payload=token_payload
        )

    @api_view(['GET'])
    def get_all(request: Request) -> Response:
        serializer = TodoResponseSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return TodoView().get_all_extract(
            params=params,
            token_payload=token_payload
        )

    @api_view(['GET'])
    def get(request: Request) -> Response:
        serializer = TodoResponseSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return TodoView().get_extract(
            params=params,
            token_payload=token_payload
        )

    @api_view(['PUT'])
    def update(request: Request) -> Response:
        serializer = TodoUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return TodoView().update_extract(
            params=params,
            token_payload=token_payload
        )

    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        serializer = TodoResponseSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return TodoView().delete_extract(
            params=params,
            token_payload=token_payload
        )
