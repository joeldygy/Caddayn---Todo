from dataclasses import dataclass


@dataclass
class SongDTO:
    title: str
    artist_id: str
    album: str = ""
    is_favorite: bool = False
