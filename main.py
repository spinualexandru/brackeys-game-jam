import pyxel

from core.device import Device
from core.state import State
from game.player import Player


class App:
    device = Device()
    state = State()
    player = Player()

    def __init__(self):
        pyxel.init(width=self.device.width, height=self.device.height, title=self.device.title)
        pyxel.load("assets.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.player.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "", 4)
        self.player.draw()

App()
