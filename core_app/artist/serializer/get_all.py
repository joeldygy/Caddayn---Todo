from rest_framework import serializers

from core_app.artist.dataclass.create import ArtistGetAllRequest
from core_app.artist.models import Artist


class ArtistGetAllRequestSerializer(serializers.Serializer):
    model_class = Artist

    def create(self, validated_data) -> ArtistGetAllRequest:
        return ArtistGetAllRequest()
