#!/usr/bin/env python

import random

from datetime import timedelta
from sys import argv

import pandas as pd

from faker import Faker


IATA = (
    'BSB',
    'CGH',
    'CNF',
    'GIG',
    'GRU',
    'POA',
    'REC',
    'SDU',
)


def generate_booking(records=1000):
    fake = Faker('pt_BR')

    data = []

    for _ in range(records):
        first_name = fake.first_name()
        last_name  = fake.last_name()
        birthday   = fake.date_of_birth(minimum_age=1, maximum_age=101).strftime('%Y-%m-%d')
        document   = fake.ssn()

        departure_date = fake.date_between(start_date='+1d', end_date='+30d')
        arrival_date   = departure_date + timedelta(days=random.randint(3, 10))

        departure_date = departure_date.strftime('%Y-%m-%d')
        arrival_date   = arrival_date.strftime('%Y-%m-%d')

        departure_iata, arrival_iata = random.sample(IATA, 2)

        data.append({
            'first_name'     : first_name,
            'last_name'      : last_name,
            'birthday'       : birthday,
            'document'       : document,
            'departure_date' : departure_date,
            'departure_iata' : departure_iata,
            'arrival_iata'   : arrival_iata,
            'arrival_date'   : arrival_date,
        })

    return pd.DataFrame(data)


def main():
    booking = generate_booking()

    print(booking.head())

    booking.to_excel('booking.xlsx', index=False)


if __name__ == '__main__':
    main()
