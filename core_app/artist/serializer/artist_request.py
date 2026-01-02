from rest_framework import serializers
from core_app.artist.dataclass import ArtistDTO


class ArtistCreateRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    bio = serializers.CharField(allow_blank=True)

    def to_dto(self):
        return ArtistDTO(
            name=self.validated_data.get("name"),
            bio=self.validated_data.get("bio", "")
        )


class ArtistUpdateRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    bio = serializers.CharField(allow_blank=True)

    def to_dto(self, existing):
        return ArtistDTO(
            name=self.validated_data.get("name", existing.name),
            bio=self.validated_data.get("bio", existing.bio),
        )
