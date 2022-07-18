from abc import abstractmethod, ABC


class WrenchInterface(ABC):
    @abstractmethod
    def socket_size(self):
        pass


class BoltInterface(ABC):
    @abstractmethod
    def bolt_size(self):
        pass


class SocketWrench(WrenchInterface):
    def socket_size(self):
        made_in = "1/2-inch"
        print(made_in)


class Bolt(BoltInterface):
    def bolt_size(self):
        hex_size = "5/8-inch"
        print(hex_size)


class BoltAdapter(WrenchInterface):
    def __init__(self, bolt):
        self.bolt = bolt

    def socket_size(self):
        self.bolt.bolt_size()


sw = SocketWrench()
sw.socket_size()

bt = Bolt()
bt.bolt_size()

ba = BoltAdapter(bt)
ba.socket_size()
