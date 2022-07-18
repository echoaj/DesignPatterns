from random import*


class Square:
    def __init__(self, hue):
        self.color = hue
        self.x_pos = None
        self.y_pos = None
        self.size = 100

    def set_coordinate(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def draw_square(self):
        print(f'Square | COLOR: {self.color}\t| X: {self.x_pos} | Y: {self.y_pos} | SIZE: {self.size}')


class Factory:
    versions = {}

    def get_square(self, key_color):
        if key_color in self.versions:
            print("\t", end='')
            return self.versions[key_color]
        else:
            print("NEW ", end='')
            new_square = Square(key_color)
            self.versions.update({key_color: new_square})
            return new_square


picker = ["blue", "green", "yellow", "purple", "orange"]

for i in range(20):
    color = choice(picker)
    x = randint(100, 999)
    y = randint(100, 999)

    produce = Factory()
    square = produce.get_square(color)
    square.set_coordinate(x, y)
    square.draw_square()

