import pygame as pg
from maps import *
from mathlib import *
from utils import *

wx, wy = 1600, 900




class Sprite:
    def __init__(self, wn: pg.Surface, pos: Vector2, scale: Vector2, color: str):
        self.wn = wn
        self.pos = pos
        self.scale = scale
        self.color = color
    def Render(self):
        drawRect(self.wn, self.pos, self.scale, self.color)
        
        
class Camera:
    def __init__(self, wn: pg.Surface, pos: Vector2, rot: float, fov: float, near: float, n: int):
        self.wn = wn
        self.pos = pos
        self.rot = rot
        self.fov = fov
        self.near = near
        self.n = n
    def calc(self):
        x = self.near * math.tan(self.fov/2 * PI/180)
        self.D = self.near/x*self.wn.get_width()
        self.H = x * self.wn.get_height()/self.wn.get_width()
    def forward(self) -> Vector2:
        return Vector2(math.sin(self.rot/180*PI), math.cos(self.rot/180*PI))
    def right(self) -> Vector2:
        return Vector2(math.sin((self.rot+90)/180*PI), math.cos((self.rot+90)/180*PI))
    def RenderLines(self):
        i = 0
        sliceWidth = self.wn.get_width() / self.n
        slicePos = -self.wn.get_width()/2 + sliceWidth/2
        if(sliceWidth != int(sliceWidth)): print("[WARNING]: Slices have non integer value, may cause bad redering")
        while(i < self.n):
            angle = math.atan(slicePos/self.D) * 180/PI + self.rot
            ray = Ray.fromAngle(self.pos, angle)
            T = INF
            for seg in map1:
                t = ray.intersect(seg)
                if(t >= self.near): T = min(t, T)
            if(T != INF):
                c = self.near / math.cos((angle-self.rot)/180*PI)
                h = wallHeight/T*c
                H = h/self.H * self.wn.get_height()
                r = 0.8**math.log(T*0.02+2, math.sqrt(2))*255
                #r = int(191-T**4/30000000*math.cos(t/2500))
                color = colorFromDist(T, (1, 0.125, 0.125))
                drawRect(self.wn, Vector2(slicePos,0), Vector2(sliceWidth, H), color)
            
            slicePos += sliceWidth
            i += 1
    def RenderMatrix(self):
        return
    def RenderSingleEntities(self):
        for e in singleEntities:
            p = e.pos - self.pos
            p.rotate(-self.rot)
            if(p.pos.y <= 0): continue
            #check collision with some ray