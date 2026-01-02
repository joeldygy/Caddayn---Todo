from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



def get_all_artists():
    return Artist.objects.all()


def create_artist(data):
    return Artist.objects.create(**data)


def get_artist(id):
    return Artist.objects.get(pk=id)


def update_artist(id, data):
    artist = Artist.objects.get(pk=id)
    for key, value in data.items():
        setattr(artist, key, value)
    artist.save()
    return artist


def delete_artist(id):
    Artist.objects.get(pk=id).delete()
