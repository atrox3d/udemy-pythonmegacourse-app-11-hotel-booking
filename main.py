import pandas as pd


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """books a hotel by changing its availability to no"""
        df.loc[df.id == self.hotel_id, 'available'] = "no"
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """ checks if the hotel is available"""
        avalaibility = df[df.id == self.hotel_id].available.squeeze()
        print(type(avalaibility))
        if avalaibility == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


if __name__ == '__main__':
    df = pd.read_csv('hotels.csv', dtype={'id': str})
    print(df)
    hotel_id = input('Enter id of the hotel: ')
    hotel = Hotel(hotel_id=hotel_id)
    if hotel.available():
        hotel.book()
        name = input('Enter your name: ')
        ticket = ReservationTicket(name, hotel)
        receipt = ticket.generate()
        print(receipt)
    else:
        print('hotel is not free')

