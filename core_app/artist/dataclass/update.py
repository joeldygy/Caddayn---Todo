from dataclasses import dataclass
from typing import Optional


@dataclass
class ArtistUpdateRequest:
    name: Optional[str] = None
    bio: Optional[str] = None
