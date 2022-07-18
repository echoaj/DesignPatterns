

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.amendment1 = "freedom of speech"
        self.amendment2 = "right to bear arms"
        self.amendment3 = "soilders in home"

    def print_amendments(self):
        print(self.amendment1)
        print(self.amendment2)
        print(self.amendment3)

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    if (id(s1) == id(s2)):
        print( "Same")
    else:
        print ("Different")

    s2.print_amendments()