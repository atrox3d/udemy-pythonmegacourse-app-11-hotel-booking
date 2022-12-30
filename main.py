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


class SpaHotel(Hotel):
    def book_package(self):
        pass


class SpaTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        thank you for your reservation!
        Here are your SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card = dict(
            number=self.number,
            expiration=expiration,
            holder=holder,
            cvc=cvc
        )
        if card in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, password):
        pwd = df_secure.loc[df_secure.number == self.number, 'password'].squeeze()
        if pwd == password:
            return True
        else:
            return False


if __name__ == '__main__':
    df = pd.read_csv('hotels.csv', dtype={'id': str})
    df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
    df_secure = pd.read_csv('card_security.csv', dtype=str)
    print(df.to_string(index=False))
    hotel_id = input('Enter id of the hotel: ')
    hotel = SpaHotel(hotel_id=hotel_id)
    if hotel.available():
        # card_number = input('Enter credit card number: ')
        card = SecureCreditCard(number='1234')
        if card.validate(expiration='12/26', holder='JOHN SMITH', cvc='123'):
            if card.authenticate(password='mypass'):
                hotel.book()
                name = input('Enter your name: ')
                ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
                receipt = ticket.generate()
                print(receipt)

                package = input('Do you want to book a spa package? ')
                if package == 'yes':
                    hotel.book_package()
                    spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                    print(spa_ticket.generate())
            else:
                print('Credit Card authentication failed')
        else:
            print('there was a problem with your payment')
    else:
        print('hotel is not free')

