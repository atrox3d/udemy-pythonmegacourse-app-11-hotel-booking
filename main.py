import pandas as pd


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
        avalaibility = df[df.id == self.hotel_id].available.squeeze()
        # print(type(avalaibility))
        if avalaibility == 'yes':
            return True
        else:
            return False


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
    # print(df.info())
    print(df.to_string(index=False))
    hotel_id = input('Enter id of the hotel: ')
    hotel = Hotel(hotel_id=hotel_id)
    if hotel.available():
        hotel.book()
        name = input('Enter your name: ')
        ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
        receipt = ticket.generate()
        print(receipt)
    else:
        print('hotel is not free')

