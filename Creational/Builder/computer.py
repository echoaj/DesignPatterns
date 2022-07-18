
class Computer:
    def __init__(self, b, m, p, g):
        self.brand = b
        self.memory = m
        self.processor = p
        self.graphics_card = g

    def __str__(self):
        return f"""-------SPECS-------\nBrand: {self.brand}\tMemory: {self.memory}\nProcessor: {self.processor}\tGraphics Card: {self.graphics_card}"""


class ComputerBuilder:
    brand = None
    memory = None
    processor = None
    graphics_card = None

    def set_brand(self, b):
        self.brand = b
        return self

    def set_memory(self, m):
        self.memory = m
        return self

    def set_processor(self, p):
        self.processor = p
        return self

    def set_graphics_card(self, g):
        self.graphics_card = g
        return self

    def get_new_computer(self):
        return Computer(self.brand, self.memory, self.processor, self.graphics_card)


builder = ComputerBuilder()
builder.set_memory("1TB")
builder.set_processor("Intel I5")

computer = builder.get_new_computer()
print(computer)





