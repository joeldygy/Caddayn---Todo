from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from core_app.song.views import SongView
from core_app.song.serializer.song_request import SongCreateRequestSerializer
from core_app.song.serializer.song_request import SongUpdateRequestSerializer
from core_app.song.serializer.song_response import SongResponseSerializer
from core_app.common.utils import CommonUtils


class SongController:

    @api_view(['POST'])
    def create(request: Request) -> Response:
        serializer = SongCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return SongView().create_extract(
            params=params,
            token_payload=token_payload
        )

    @api_view(['GET'])
    def get_all(request: Request) -> Response:
        serializer = SongResponseSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return SongView().get_all_extract(
            params=params,
            token_payload=token_payload
        )


    @api_view(['GET'])
    def get(request: Request) -> Response:
        serializer = SongResponseSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return SongView().get_extract(
            params=params,
            token_payload=token_payload
        )

    @api_view(['PUT'])
    def update(request: Request) -> Response:
        serializer = SongUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()


