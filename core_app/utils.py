# core_app/utils.py

import pandas as pd

class TodoUtils:
    def __init__(self):
        # Map database column names → API response names
        self.mapped_column_names = {
            "title": "task_title",
            "description": "task_description",
            "is_completed": "completed"
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
