from rest_framework import serializers
from core_app.song.dataclass import SongDTO


class SongCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    artist_id = serializers.CharField(max_length=255)
    album = serializers.CharField(allow_blank=True)
    is_favorite = serializers.BooleanField(default=False)

    def to_dto(self):
        return SongDTO(
            title=self.validated_data.get("title"),
            artist_id=self.validated_data.get("artist"),
            album=self.validated_data.get("album", ""),
            is_favorite=self.validated_data.get("is_favorite", False)
        )


class SongUpdateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    artist_id = serializers.CharField(max_length=255)
    album = serializers.CharField(allow_blank=True)
    is_favorite = serializers.BooleanField()

    def to_dto(self, existing):
        return SongDTO(
            title=self.validated_data.get("title", existing.title),
            artist_id=self.validated_data.get("artist", existing.artist),
            album=self.validated_data.get("album", existing.album),
            is_favorite=self.validated_data.get("is_favorite", existing.is_favorite),
        )
