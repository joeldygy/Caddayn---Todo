from rest_framework import serializers
from core_app.artist.dataclass.create import ArtistDTO


class ArtistResponseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    bio = serializers.CharField()

    @staticmethod
    def from_dto(artist_dto: ArtistDTO):
        return {
            "name": artist_dto.name,
            "bio": artist_dto.bio
        }
