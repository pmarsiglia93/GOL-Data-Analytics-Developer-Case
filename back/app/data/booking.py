import io

import pandas as pd


class BookingData:
    @classmethod
    def read_from_file(cls, content: bytes) -> pd.DataFrame:
        if isinstance(content, bytes):
            content = io.BytesIO(content)

        df = pd.read_excel(
            content,
            dtype={
                'first_name'     : str,
                'last_name'      : str,
                'birthday'       : str,
                'document'       : str,
                'departure_date' : str,
                'departure_iata' : str,
                'arrival_iata'   : str,
                'arrival_date'   : str,
            }
        )

        return df
