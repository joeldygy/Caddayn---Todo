from rest_framework import serializers
from core_app.song.dataclass import SongDTO


class SongResponseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    artist = serializers.CharField(max_length=255)
    album = serializers.CharField()
    is_favorite = serializers.BooleanField()

    @staticmethod
    def from_dto(song_dto: SongDTO):
        return {
            "title": song_dto.title,
            "artist": song_dto.artist,
            "album": song_dto.album,
            "is_favorite": song_dto.is_favorite
        }
