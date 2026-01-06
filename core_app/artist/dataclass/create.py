from dataclasses import dataclass


@dataclass
class ArtistCreateRequest:
    name: str
    bio: str = ""
