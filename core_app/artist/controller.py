from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from core_app.artist.views import ArtistView
from core_app.artist.serializer.artist_request import (
    ArtistCreateRequestSerializer,
    ArtistUpdateRequestSerializer
)
from core_app.artist.serializer.artist_response import ArtistResponseSerializer
from core_app.common.utils import CommonUtils


class ArtistController:

    @api_view(['POST'])
    def create(request: Request) -> Response:
        serializer = ArtistCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return ArtistView().create_extract(
            params=params,
            token_payload=token_payload
        )

    @api_view(['GET'])
    def get_all(request: Request) -> Response:
        serializer = ArtistResponseSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return ArtistView().get_all_extract(
            params=params,
            token_payload=token_payload
        )

    @api_view(['GET'])
    def get(request: Request) -> Response:
        serializer = ArtistResponseSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return ArtistView().get_extract(
            params=params,
            token_payload=token_payload
        )

    @api_view(['PUT'])
    def update(request: Request) -> Response:
        serializer = ArtistUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return ArtistView().update_extract(
            params=params,
            token_payload=token_payload
        )

    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        serializer = ArtistResponseSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        params = serializer.to_dto()
        token_payload = CommonUtils.get_token_payload(request)

        return ArtistView().delete_extract(
            params=params,
            token_payload=token_payload
        )
