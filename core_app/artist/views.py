from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core_app.common.utils import CommonUtils
from core_app.artist.models import (
    get_all_artists,
    create_artist,
    get_artist,
    update_artist,
    delete_artist
)

from core_app.artist.serializer.artist_request import (
    ArtistCreateRequestSerializer,
    ArtistUpdateRequestSerializer
)

from core_app.artist.serializer.artist_response import ArtistResponseSerializer
from core_app.artist.utils import ArtistUtils
from core_app.common.decorators import standard_response


class ArtistView:

    @api_view(['GET'])
    def artist_list(self, request):
        artists = get_all_artists()
        serializer = ArtistResponseSerializer(artists, many=True)

        # map using utils
        mapped = ArtistUtils().mapper(serializer.data)

        return Response(
            data={"message": "Artists fetched successfully", "data": mapped},
            status=status.HTTP_200_OK
        )

    @api_view(['POST'])
    def artist_create(self, request):
        serializer = ArtistCreateRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "status": False,
                    "message": "Validation failed",
                    "errors": serializer.errors
                }
            )

        dto = serializer.to_dto()
        create_artist(dto.__dict__)

        return Response(
            status=status.HTTP_201_CREATED,
            data=CommonUtils.success_response(
                message="Artist successfully created"
            )
        )

    @api_view(['GET'])
    def artist_detail(self, request, id):
        try:
            artist = get_artist(id)
        except Exception:
            return Response(
                {"message": "Artist not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ArtistResponseSerializer(artist)
        return Response(
            data={"message": "Artist fetched successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    @api_view(['PUT'])
    def artist_update(self, request, id):
        try:
            existing = get_artist(id)
        except Exception:
            return Response(
                {"message": "Artist not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ArtistUpdateRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        dto = serializer.to_dto(existing)
        updated = update_artist(id, dto.__dict__)

        return Response(
            data={
                "message": "Artist updated successfully",
                "data": ArtistResponseSerializer(updated).data
            },
            status=status.HTTP_200_OK
        )

    @api_view(['DELETE'])
    def artist_delete(self, request, id):
        try:
            delete_artist(id)
        except Exception:
            return Response(
                {"message": "Artist not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            status=status.HTTP_200_OK,
            data=CommonUtils.success_response(
                message="Artist successfully deleted"
            )
        )
