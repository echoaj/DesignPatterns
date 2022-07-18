from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next_chain(self, next):
        pass

    @abstractmethod
    def calculate(self):
        pass


class Operation:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operand = operator


class Add(Handler):
    next_chain = None

    def set_next_chain(self, next_object):
        self.next_chain = next_object

    def calculate(self, req):
        if req.operand == '+':
            print(f'{req.num1} + {req.num2} = ', req.num1 + req.num2)
        else:
            self.next_chain.calculate(req)


class Sub(Handler):
    next_chain = None

    def set_next_chain(self, next_object):
        self.next_chain = next_object

    def calculate(self, req):
        if req.operand == '-':
            print(f'{req.num1} - {req.num2} = ', req.num1 - req.num2)
        else:
            self.next_chain.calculate(req)


class Mul(Handler):
    next_chain = None

    def set_next_chain(self, next_object):
        self.next_chain = next_object

    def calculate(self, req):
        if req.operand == '*':
            print(f'{req.num1} * {req.num2} = ', req.num1 * req.num2)
        else:
            self.next_chain.calculate(req)


class Div(Handler):
    next_chain = None

    def set_next_chain(self, next_object):
        self.next_chain = next_object

    def calculate(self, req):
        if req.operand == '/':
            print(f'{req.num1} / {req.num2} = ', req.num1 / req.num2)
        else:
            print("Operations available:  + - * /")


chain1_add = Add()
chain2_sub = Sub()
chain3_mul = Mul()
chain4_div = Div()

chain1_add.set_next_chain(chain2_sub)
chain2_sub.set_next_chain(chain3_mul)
chain3_mul.set_next_chain(chain4_div)

request = Operation(150, 90, "*")
chain1_add.calculate(request)
