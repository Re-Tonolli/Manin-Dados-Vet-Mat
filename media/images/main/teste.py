from manim import *


class Tornar(Scene):
    def construct(self):
        quadrado = Square()
        quadrado.become(Circle())
        self.add(quadrado)

quadrado.become(Circle())
self.play(FadeIn(quadrado))
self.wait(2)
