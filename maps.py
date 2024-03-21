from mathlib import *
import collections

wallHeight = 2
corner = 10
corners = [Vector2(-corner,-corner), Vector2(-corner,corner), Vector2(corner,corner), Vector2(corner,-corner)]
singleEntities = collections.deque()  #entities which need only one ray to render

map1 = [
    Line(corners[0], corners[1]),
    Line(corners[1], corners[2]),
    Line(corners[2], corners[3]),
    Line(corners[3], corners[0]),
    Line(Vector2(-5,-5),Vector2(-5,2))
]

minimap = (Vector2(-12,12), Vector2(12,-12))