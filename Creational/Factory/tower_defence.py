from random import *


class Enemy:
    def __init__(self, tp, pw, sp, cr, sx, sy):
        self.typeof = tp
        self.power = pw
        self.speed = sp
        self.color = cr
        self.sizeX = sx
        self.sizeY = sy
        self.x_pos = 800
        self.y_pos = randint(380, 500)

    def move(self):
        print(f'rgb{self.color}')
        self.x_pos -= self.speed


class FatEnemy(Enemy):
    def __init__(self):
        name = "Fat"
        damage = 10
        speed = 1
        rgb = (50, 80, 200)
        size_x = 40
        size_y = 40
        super(FatEnemy, self).__init__ \
            (name, damage, speed, rgb, size_x, size_y)

    def move(self):
        super(FatEnemy, self).move()
        print(f'triangle({self.x_pos}, {self.y_pos}, {self.sizeX}, {self.sizeY})\n')


class NormalEnemy(Enemy):
    def __init__(self):
        name = "Normal"
        damage = 5
        speed = 1
        rgb = (180, 240, 130)
        size_x = 10
        size_y = 20
        super(NormalEnemy, self).__init__ \
            (name, damage, speed, rgb, size_x, size_y)

    def move(self):
        super(NormalEnemy, self).move()
        print(f'square({self.x_pos}, {self.y_pos}, {self.sizeX}, {self.sizeY})\n')


class FastEnemy(Enemy):
    def __init__(self):
        name = "Fast"
        damage = 3
        speed = 3
        rgb = (220, 40, 70)
        size_x = 20
        size_y = 10
        super(FastEnemy, self).__init__ \
            (name, damage, speed, rgb, size_x, size_y)

    def move(self):
        super(FastEnemy, self).move()
        print(f'circle({self.x_pos}, {self.y_pos}, {self.sizeX}, {self.sizeY})\n')


class EnemyFactory():
    def select_enemy(self, pick):
        if pick == 'fat':
            return FatEnemy()
        elif pick == 'normal':
            return NormalEnemy()
        elif pick == 'fast':
            return FastEnemy()


enemy = EnemyFactory()

fat_enemy = enemy.select_enemy("fat")
fat_enemy.move()

normal_enemy = enemy.select_enemy("normal")
normal_enemy.move()

fast_enemy = enemy.select_enemy("fast")
fast_enemy.move()
