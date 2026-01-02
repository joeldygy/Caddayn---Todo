from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.TextField(blank=True)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def get_all_songs():
    return Song.objects.all()


def create_song(data):
    return Song.objects.create(**data)


def get_song(id):
    return Song.objects.get(pk=id)


def update_song(id, data):
    song = Song.objects.get(pk=id)
    for key, value in data.items():
        setattr(song, key, value)
    song.save()
    return song


def delete_song(id):
    Song.objects.get(pk=id).delete()
