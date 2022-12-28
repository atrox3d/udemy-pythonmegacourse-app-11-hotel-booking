import pandas as pd


class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass

if __name__ == '__main__':
    df = pd.read_csv('hotels.csv')
    print(df)
    id = input('Enter id of the hotel: ')
    hotel = Hotel(id=id)
    if hotel.available():
        hotel.book()
        name = input('Enter your name: ')
        ticket = ReservationTicket(name, hotel)
        receipt = ticket.generate()
        print(receipt)
    else:
        print('hotel is not free')

