

class DecimalSubject:
    def __init__(self):
        self.__decimal = None
        self.__observers = []

    def add_observer(self, obs):
        self.__observers.append(obs)

    def convert(self, num):
        self.__decimal = num
        for obs in self.__observers:
            obs.update(self.__decimal)


class HexadecimalObserver:
    @staticmethod
    def update(num):
        print(f'{num} in HEX = {hex(num)}')


class OctalObserver:
    @staticmethod
    def update(num):
        print(f'{num} in OCT = {oct(num)}')
        

class BinaryObserver:
    @staticmethod
    def update(num):
        print(f'{num} in BIN = {bin(num)}\n')


# Observers
hexa = HexadecimalObserver()
octa = OctalObserver()
bina = BinaryObserver()

# Subject
deci = DecimalSubject()

deci.add_observer(hexa)
deci.add_observer(octa)
deci.add_observer(bina)

deci.convert(8)
deci.convert(-50)
deci.convert(100)

