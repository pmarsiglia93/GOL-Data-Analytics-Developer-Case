import io
import pandas as pd

class BookingData:
    @classmethod
    def read_from_file(cls, content: bytes) -> pd.DataFrame:
        if isinstance(content, bytes):
            # Tenta ler como Excel
            try:
                df = pd.read_excel(
                    io.BytesIO(content),
                    dtype={
                        'first_name': str,
                        'last_name': str,
                        'birthday': str,
                        'document': str,
                        'departure_date': str,
                        'departure_iata': str,
                        'arrival_iata': str,
                        'arrival_date': str,
                    },
                    engine='openpyxl'
                )
                return df
            except Exception as e:
                print("Error reading Excel file:", e)
            # Tenta CSV
            try:
                df = pd.read_csv(
                    io.StringIO(content.decode('utf-8')),
                    dtype={
                        'first_name': str,
                        'last_name': str,
                        'birthday': str,
                        'document': str,
                        'departure_date': str,
                        'departure_iata': str,
                        'arrival_iata': str,
                        'arrival_date': str,
                    }
                )
                return df
            except Exception as e:
                print("Error reading CSV file:", e)
        raise ValueError("Invalid data or file format")

    @classmethod
    def validate_dataframe(cls, df: pd.DataFrame) -> pd.DataFrame:
        required_columns = [
            'first_name',
            'last_name',
            'birthday',
            'document',
            'departure_date',
            'departure_iata',
            'arrival_iata',
            'arrival_date',
        ]
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns: {', '.join(missing_columns)}")
        df.columns = df.columns.str.strip()
        return df
