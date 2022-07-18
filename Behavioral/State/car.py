from abc import ABC


class CarState(object):
    current_state = None
    allowed_states = []

    def switch_state(self, requested):
        name = requested.current_state
        if name in self.allowed_states:
            print(f'Current: {self.current_state} -> switching to {name}')
            self.__class__ = requested
        else:
            print(f'Current: {self.current_state} -> \033[31mRequest \"{name}\" Denied\033[0m')

    def __str__(self):
        return self.current_state


class Off(CarState):
    current_state = 'Off'
    allowed_states = ["On"]


class On(CarState):
    current_state = 'On'
    allowed_states = ["Off", "Drive"]


class Drive(CarState):
    current_state = 'Drive'
    allowed_states = ["On"]


class Car(object):
    def __init__(self):
        self.state = Off()

    def change_state(self, request):
        self.state.switch_state(request)


car = Car()
car.change_state(Off)
car.change_state(On)
car.change_state(Drive)
car.change_state(Off)
car.change_state(On)
car.change_state(Off)
car.change_state(Drive)
