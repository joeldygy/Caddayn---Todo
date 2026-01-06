from rest_framework import serializers

from core_app.artist.dataclass.create import ArtistCreateRequest
from core_app.common.common import Common
from core_app.artist.models import Artist


class ArtistCreateRequestSerializer(serializers.Serializer):
    model_class = Artist

    name = serializers.CharField(max_length=255)
    bio = serializers.CharField(required=False, allow_blank=True)

    def validate_name(self, value):
        if not Common.regex_check(value):
            raise serializers.ValidationError(
                "Artist name should only contain letters, numbers, spaces, and common special characters (&, @, ., _)"
            )
        return value

    def create(self, validated_data) -> ArtistCreateRequest:
        return ArtistCreateRequest(**validated_data)
