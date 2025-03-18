import pandas as pd


class DashboardData:
    # Passenger departures per date
    @classmethod
    def get_chart_data_1(cls, dataframe: pd.DataFrame) -> list[dict]:
        df = dataframe.copy()

        df = df['departure_date'].value_counts().sort_index().reset_index()

        data = df.set_axis(['category', 'value'], axis=1).to_dict(orient='records')

        return data

    # Passenger arrivals per date
    @classmethod
    def get_chart_data_2(cls, dataframe: pd.DataFrame) -> list[dict]:
        df = dataframe.copy()

        df = df['arrival_date'].value_counts().sort_index().reset_index()

        data = df.set_axis(['category', 'value'], axis=1).to_dict(orient='records')

        return data

    # Passengers per route
    @classmethod
    def get_chart_data_3(cls, dataframe: pd.DataFrame) -> list[dict]:
        df = dataframe.copy()

        df['iatapair'] = df['departure_iata'] + df['arrival_iata']

        df = df['iatapair'].value_counts().sort_index().reset_index()

        data = df.set_axis(['category', 'value'], axis=1).to_dict(orient='records')

        return data

    # Passenger departures and arrivals per date and route
    @classmethod
    def get_data(cls, dataframe: pd.DataFrame) -> list[dict]:
        df = dataframe.copy()

        df['iatapair'] = df['departure_iata'] + df['arrival_iata']

        departures = df.groupby(['departure_date', 'iatapair']).size()
        arrivals = df.groupby(['arrival_date', 'iatapair']).size()

        departures = departures.reset_index(name='departures').rename(columns={'departure_date': 'date'})
        arrivals = arrivals.reset_index(name='arrivals').rename(columns={'arrival_date': 'date'})

        df = pd.merge(departures, arrivals, how='outer', on=['date', 'iatapair']).fillna(0)

        df['departures'] = df['departures'].astype(int)
        df['arrivals'] = df['arrivals'].astype(int)

        df = df.sort_values(by=['date', 'iatapair'], ignore_index=True).to_dict(orient='records')

        return df
