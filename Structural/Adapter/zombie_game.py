from abc import abstractmethod, ABC


class ZombieInterface(ABC):
    @abstractmethod
    def hit(self):
        pass
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def eat(self):
        pass


class PlayerInterface(ABC):
    @abstractmethod
    def shoot(self):
        pass
    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def kill(self):
        pass


class Zombie(ZombieInterface):
    def hit(self):
        print("Hit does 25 damage")
    def run(self):
        print("Running at 10mph")
    def eat(self):
        print("Eating player's Brains")


class Human(PlayerInterface):
    def shoot(self):
        print("Shoot does 50 damage")
    def walk(self):
        print("Walking at 3mph")
    def kill(self):
        print("Killed Zombie")


class HumanAdapter(ZombieInterface):
    def __init__(self, person):
        self.human = person
    def hit(self):
        self.human.shoot()
    def run(self):
        self.human.walk()
    def eat(self):
        self.human.kill()


hum = Human()
hum.shoot()
hum.walk()
hum.kill()

print()

zom = Zombie()
zom.hit()
zom.run()
zom.eat()

print()

adp = HumanAdapter(hum)
adp.hit()
adp.run()
adp.eat()
