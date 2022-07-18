from random import*


class Greeting:
    def __init__(self, n):
        self.name = n

    def welcome(self):
        print(f'Welcome {self.name} To The Joslin Hotel!')


class ConfirmReservation:
    def __init__(self, res):
        self.reservation = res

    def is_valid(self):
        if self.reservation.isdigit():
            return True
        else:
            return False


class ConfirmID:
    def __init__(self, i):
        self.id = i

    def is_valid(self):
        if len(self.id) == 7:
            return True
        else:
            return False


class Accepted:
    def __init__(self, bol1, bol2):
        self.check_reservation = bol1
        self.check_id = bol2

    def result(self):
        if self.check_reservation and self.check_id:
            print("You may enter.")
            print(f"Your room number is {randint(100,999)}.")
        else:
            print("Sorry your credentials have been revoked.")


class Facade:
    def __init__(self, name, cr, ci):
        self.greeting = Greeting(name)
        self.customer_reservation = ConfirmReservation(cr)
        self.confirm_id = ConfirmID(ci)

    def check_in(self):
        self.greeting.welcome()
        res_bool = self.customer_reservation.is_valid()
        id_bool = self.confirm_id.is_valid()
        Accepted(res_bool, id_bool).result()


hotel = Facade("Alex", "76479382730", "1817974")
hotel.check_in()











