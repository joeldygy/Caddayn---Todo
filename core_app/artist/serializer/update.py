from rest_framework import serializers

from core_app.artist.dataclass.create import ArtistUpdateRequest
from core_app.common.common import Common
from core_app.artist.models import Artist


class ArtistUpdateRequestSerializer(serializers.Serializer):
    model_class = Artist

    name = serializers.CharField(max_length=255, required=False)
    bio = serializers.CharField(required=False, allow_blank=True)

    def validate_name(self, value):
        if not Common.regex_check(value):
            raise serializers.ValidationError(
                "Artist name should only contain letters, numbers, spaces, and common special characters (&, @, ., _)"
            )
        return value

    def create(self, validated_data) -> ArtistUpdateRequest:
        return ArtistUpdateRequest(**validated_data)
