from rest_framework import serializers

from core_app.artist.dataclass.create import ArtistDeleteRequest
from core_app.artist.models import Artist
from core_app.common.constants import StaticLimits


class ArtistDeleteRequestSerializer(serializers.Serializer):
    model_class = Artist

    artist_code = serializers.CharField(max_length=StaticLimits.code_limit)

    def create(self, validated_data) -> ArtistDeleteRequest:
        return ArtistDeleteRequest(**validated_data)
