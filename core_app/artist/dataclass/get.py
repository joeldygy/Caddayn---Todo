from dataclasses import dataclass
from typing import Optional


@dataclass
class ArtistGetRequest:
    artist_code: Optional[str] = None
