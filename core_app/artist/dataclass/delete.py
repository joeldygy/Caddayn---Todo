from dataclasses import dataclass


@dataclass
class ArtistDeleteRequest:
    artist_code: str
