import math
import pyxel


class Player:
    x = 50
    y = 50
    width = 16
    height = 16
    speed = 2
    is_jumping = False
    jump_height = 20

    def __init__(self, **kwargs):
        self.x = kwargs.get("x", self.x)
        self.y = kwargs.get("y", self.y)
        self.width = kwargs.get("width", self.width)
        self.height = kwargs.get("height", self.height)
        self.speed = kwargs.get("speed", self.speed)
        self.jump_index = 0

    def move(self, dx, dy):
        max_width = pyxel.screen.width
        max_height = pyxel.screen.height

        if dx != 0:
            self.x += dx * self.speed
            self.x = max(0, min(self.x, max_width - self.width))

        if dy != 0:
            self.y += dy * self.speed
            self.y = max(0, min(self.y, max_height - self.height))

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_index = 0
            self.original_y = self.y

    def handle_jump(self):
        if self.is_jumping:
            self.jump_index += 1
            self.y = self.original_y - math.sin(math.pi * self.jump_index / self.jump_height) * self.jump_height
            if self.jump_index >= self.jump_height:
                self.y = self.original_y
                self.is_jumping = False

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.jump()

        if pyxel.btnp(pyxel.KEY_W, repeat=True, hold=1):
            self.move(0, -1)
        elif pyxel.btnp(pyxel.KEY_S, repeat=True, hold=1):
            self.move(0, 1)
        if pyxel.btnp(pyxel.KEY_A, repeat=True, hold=1):
            self.move(-1, 0)
        elif pyxel.btnp(pyxel.KEY_D, repeat=True, hold=1):
            self.move(1, 0)

        self.handle_jump()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.width, self.height)
