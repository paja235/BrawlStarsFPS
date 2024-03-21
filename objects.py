from mathlib import *

class Bullet:
    def __init__(self, pos: Vector2, size: Vector2, color: str):
        self.pos = pos
        self.size = size
        self.color = color