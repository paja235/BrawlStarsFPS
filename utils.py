import pygame as pg
from mathlib import *

#math
def convertCoords(wn: pg.Surface, c) -> tuple:
    if(type(c) == tuple): return (wn.get_width()/2+c[0], wn.get_height()/2-c[1])
    elif(type(c) == Vector2): return (wn.get_width()/2+c.x, wn.get_height()/2-c.y)
    else: assert(False)

#drawing
def drawRect(wn: pg.Surface, pos: Vector2, scale: Vector2, color: str):
    pg.draw.rect(wn, color, (wn.get_width()/2-scale.x/2+pos.x, wn.get_height()/2-scale.y/2-pos.y, scale.x, scale.y))
def drawCircle(wn: pg.Surface, pos: Vector2, radius: int, color: str):
    pg.draw.circle(wn, color, convertCoords(wn, pos), radius)
def drawLine(wn: pg.Surface, begin: Vector2, end: Vector2, color: str, width: int = 1):
    pg.draw.line(wn, color, convertCoords(wn, begin), convertCoords(wn, end), width)
   
#colors
def colorFromTuple(t: tuple) -> str:
    r = int(min(max(t[0],0),255))
    g = int(min(max(t[1],0),255))
    b = int(min(max(t[2],0),255))
    return "#{:02x}{:02x}{:02x}".format(r,g,b)
def colorFromDist(dist: float, c: tuple):
    r = 0.8**math.log(dist*0.02+2, math.sqrt(2))*255
    return colorFromTuple((c[0]*r, c[1]*r, c[2]*r))