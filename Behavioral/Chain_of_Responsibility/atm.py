from abc import ABCMeta, abstractmethod


class ATMHandler(metaclass=ABCMeta):
    @abstractmethod
    def set_next_chain(self, next_chain):
        pass

    @abstractmethod
    def dispense(self, process):
        pass


class ATM:
    def __init__(self, cash):
        self.if_valid(cash)
        self.money = cash
        self.hundreds = None
        self.fifties = None
        self.twenties = None
        self.tens = None

    @staticmethod
    def if_valid(cash):
        if cash % 10 != 0:
            print("REQUEST DENIED")
            print("Bills of 10 or above only!")
        else:
            print("REQUEST GRANTED\n")

    def display_money(self):
        print("Hundreds: ", self.hundreds)
        print("Fifties: ", self.fifties)
        print("Twenties: ", self.twenties)
        print("Tens: ", self.tens)


class DispenseHundreds(ATMHandler):
    next_event = None
    fifties = None

    def set_next_chain(self, next_chain):
        self.fifties = next_chain

    def dispense(self, process):
        process.hundreds = int(process.money / 100)
        process.money -= 100 * process.hundreds
        self.fifties.dispense(process)


class DispenseFifties(ATMHandler):
    next_event = None
    twenties = None

    def set_next_chain(self, next_chain):
        self.twenties = next_chain

    def dispense(self, process):
        process.fifties = int(process.money / 50)
        process.money -= 50 * process.fifties
        self.twenties.dispense(process)


class DispenseTwenties(ATMHandler):
    next_event = None
    tens = None

    def set_next_chain(self, next_chain):
        self.tens = next_chain

    def dispense(self, process):
        process.twenties = int(process.money / 20)
        process.money -= 20 * process.twenties
        self.tens.dispense(process)


class DispenseTens(ATMHandler):
    next_event = None
    output = None

    def set_next_chain(self, next_chain):
        self.output = next_chain

    def dispense(self, process):
        process.tens = int(process.money / 10)
        process.money -= 10 * process.tens
        self.output.display_money()


request = ATM(560)
hun = DispenseHundreds()
fif = DispenseFifties()
twe = DispenseTwenties()
ten = DispenseTens()

hun.set_next_chain(fif)
fif.set_next_chain(twe)
twe.set_next_chain(ten)
ten.set_next_chain(request)


hun.dispense(request)
