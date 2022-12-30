import pandas as pd
from abc import ABC, abstractmethod


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df.id == self.hotel_id].name.squeeze()
        # print(f'{type(self.name)=}')

    def book(self):
        """books a hotel by changing its availability to no"""
        df.loc[df.id == self.hotel_id, 'available'] = "no"
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """ checks if the hotel is available"""
        availability = df[df.id == self.hotel_id].available.squeeze()
        # print(type(availability))
        if availability == 'yes':
            return True
        else:
            return False

    def __eq__(self, other):
        return self.hotel_id == other.hotel_id


class Ticket(ABC):
    @abstractmethod
    def method(self):
        pass


class AnotherTicket(Ticket):
    def method(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


if __name__ == '__main__':
    df = pd.read_csv('hotels.csv', dtype={'id': str})
    at = AnotherTicket()
