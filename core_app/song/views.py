from rest_framework.response import Response
from rest_framework import status

from core_app.common.utils import CommonUtils
from core_app.song.models import (
    get_all_songs,
    create_song,
    get_song,
    update_song,
    delete_song
)

from core_app.song.serializer.song_request import (
    SongCreateRequestSerializer,
    SongUpdateRequestSerializer
)

from core_app.song.serializer.song_response import SongResponseSerializer
from core_app.song.utils import SongUtils  # you can create this similar to TodoUtils


class SongView:

    def song_list(self, request):
        songs = get_all_songs()
        serializer = SongResponseSerializer(songs, many=True)

        # map using utils
        mapped = SongUtils().mapper(serializer.data)

        return Response(
            data={"message": "Songs fetched successfully", "data": mapped},
            status=status.HTTP_200_OK
        )

    def song_create(self, request):
        serializer = SongCreateRequestSerializer(data=request.data)

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
        create_song(dto.__dict__)

        return Response(
            status=status.HTTP_201_CREATED,
            data=CommonUtils.success_response(
                message="Song successfully created"
            )
        )

    def song_detail(self, request, id):
        try:
            song = get_song(id)
        except Exception:
            return Response(
                {"message": "Song not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SongResponseSerializer(song)
        return Response(
            data={"message": "Song fetched successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def song_update(self, request, id):
        try:
            existing = get_song(id)
        except Exception:
            return Response(
                {"message": "Song not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SongUpdateRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        dto = serializer.to_dto(existing)
        updated = update_song(id, dto.__dict__)

        return Response(
            data={
                "message": "Song updated successfully",
                "data": SongResponseSerializer(updated).data
            },
            status=status.HTTP_200_OK
        )

    def song_delete(self, request, id):
        try:
            delete_song(id)
        except Exception:
            return Response(
                {"message": "Song not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            status=status.HTTP_200_OK,
            data=CommonUtils.success_response(
                message="Song successfully deleted"
            )
        )
