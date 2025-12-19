# song/utils.py

import pandas as pd

class SongUtils:
    def __init__(self):
        # Map database column names → API response names
        self.mapped_column_names = {
            "title": "song_title",
            "artist": "song_artist",
            "album": "song_album",
            "is_favorite": "favorite"
        }

    def mapper(self, data: list) -> list:
        if not data:
            return []

        # Create DataFrame from list of dicts
        dataframe = pd.DataFrame.from_records(data)

        # Rename columns to user-friendly names
        dataframe.rename(columns=self.mapped_column_names, inplace=True)

        # Convert DataFrame back to list of dicts
        return dataframe.to_dict(orient='records')
