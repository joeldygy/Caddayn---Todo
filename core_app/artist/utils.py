import pandas as pd


class ArtistUtils:
    def __init__(self):
        self.mapped_column_names = {
            "name": "artist_name",
            "bio": "artist_bio"
        }

    def mapper(self, data: list) -> list:
        if not data:
            return []

        dataframe = pd.DataFrame.from_records(data)

        dataframe.rename(columns=self.mapped_column_names, inplace=True)

        return dataframe.to_dict(orient='records')
