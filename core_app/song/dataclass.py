from dataclasses import dataclass


@dataclass
class SongDTO:
    title: str
    artist: str
    album: str = ""
    is_favorite: bool = False
