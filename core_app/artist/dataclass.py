from dataclasses import dataclass


@dataclass
class ArtistDTO:
    name: str
    bio: str = ""
