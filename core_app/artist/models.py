from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



def get_all_artists() -> list:
    return Artist.objects.filter(is_active=True).values(
        "id",
        "name",
        "bio",
        "created_at"
    ) or []



def create_artist(self, name: str, bio: str):
    self.name = name
    self.bio = bio
    self.save()
    return self

def get_artist(artist_id: int = None, single: bool = False) -> list | dict:
    if single:
        return Artist.objects.filter(is_active=True).values(
            "id",
            "name",
            "bio",
            "created_at"
        ).first() or []
    return Artist.objects.filter(is_active=True).values(
        "id",
        "name",
        "bio",
        "created_at"
    ) or []


def update_artist(self, name: str = None, bio: str = None):
    if name is not None:
        self.name = name
    if bio is not None:
        self.bio = bio
    self.save()
    return self


def delete_artist(artist_id: int) -> None:
    Artist.objects.filter(id=artist_id).update(is_active=False)

