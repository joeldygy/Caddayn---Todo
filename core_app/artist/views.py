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

from core_app.artist.serializer.create import (
    ArtistCreateRequestSerializer,
    ArtistUpdateRequestSerializer
)

from core_app.artist.serializer.artist_response import ArtistResponseSerializer
from core_app.artist.utils import ArtistUtils
from core_app.common.decorators import standard_response


class ArtistView:

    @api_view(['GET'])
    @standard_response("Artists fetched successfully")
    def artist_list(self, request):
        artists = get_all_artists()
        serializer = ArtistResponseSerializer(artists, many=True)
        mapped = ArtistUtils().mapper(serializer.data)
        return {"data": mapped, "message": "Artists fetched successfully"}

    @api_view(['POST'])
    @standard_response("Artist successfully created")
    def artist_create(self, request):
        serializer = ArtistCreateRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return {"success": False, "message": "Validation failed", "errors": serializer.errors}

        dto = serializer.to_dto()
        create_artist(dto.__dict__)
        return {"message": "Artist successfully created"}

    @api_view(['GET'])
    @standard_response("Artist fetched successfully")
    def artist_detail(self, request, id):
        try:
            artist = get_artist(id)
        except Exception:
            return {"success": False, "message": "Artist not found"}

        serializer = ArtistResponseSerializer(artist)
        return {"data": serializer.data, "message": "Artist fetched successfully"}

    @api_view(['PUT'])
    @standard_response("Artist updated successfully")
    def artist_update(self, request, id):
        try:
            existing = get_artist(id)
        except Exception:
            return {"success": False, "message": "Artist not found"}

        serializer = ArtistUpdateRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return {"success": False, "errors": serializer.errors}

        dto = serializer.to_dto(existing)
        updated = update_artist(id, dto.__dict__)
        return {"data": ArtistResponseSerializer(updated).data, "message": "Artist updated successfully"}

    @api_view(['DELETE'])
    @standard_response("Artist successfully deleted")
    def artist_delete(self, request, id):
        try:
            delete_artist(id)
        except Exception:
            return {"success": False, "message": "Artist not found"}

        return {"message": "Artist successfully deleted"}


