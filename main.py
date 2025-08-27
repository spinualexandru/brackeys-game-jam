import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Zyth ( Alex Spinu ) Brackey's Game Jam 2025.2")
        pyxel.load("assets.pyxres")
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(1)
        pyxel.text(55, 41, "", 4)
        pyxel.blt(61, 66, 0, 0, 0, 16,16)


App()

