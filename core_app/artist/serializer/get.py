from rest_framework import serializers

from core_app.artist.dataclass.create import ArtistGetRequest
from core_app.artist.models import Artist
from core_app.common.constants import StaticLimits


class ArtistGetRequestSerializer(serializers.Serializer):
    model_class = Artist

    artist_code = serializers.CharField(
        max_length=StaticLimits.code_limit,
        required=False
    )

    def create(self, validated_data) -> ArtistGetRequest:
        return ArtistGetRequest(**validated_data)
