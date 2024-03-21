from renderer import *
import pygame as pg
import time
import brawlers
from objects import *

#shame
import copy


#ඩ
selectedBrawler = brawlers.Leon

cam = Camera(0, Vector2(0, 0), -90, 110, 0.01, 400)
rotspeed = 100

crosshair = Sprite(0, Vector2(0,0), Vector2(2,2), '#86959c')
groundColor = '#6a6a6a'
ground = Sprite(0, Vector2(0,-0.25*wy), Vector2(wx,wy/2+2), groundColor)


def renderInit(wn: pg.Surface):
    cam.wn = wn
    cam.calc()
    crosshair.wn = wn
    ground.wn = wn


def CheckCollision(mov: Vector2):
    ray = Ray(cam.pos+mov, Vector2(0,0))
    for l in map1:
        d = l.distance(cam.pos+mov, selectedBrawler.r)
        mov -= d
    return mov

def InputActions(wn: pg.Surface, dt: float):
    keys = pg.key.get_pressed()
    if(keys[pg.K_LEFT]):
        cam.rot -= rotspeed * dt
    if(keys[pg.K_RIGHT]):
        cam.rot += rotspeed * dt
        
    mov = Vector2(0,0)
    if(keys[pg.K_w]):
        mov.y += 1
    if(keys[pg.K_s]):
        mov.y -= 1
    if(keys[pg.K_d]):
        mov.x += 1
    if(keys[pg.K_a]):
        mov.x -= 1
    mov = cam.forward()*mov.y + cam.right()*mov.x
    mov.normalize()
    mov *= selectedBrawler.speed * dt
    mov = CheckCollision(mov)
    cam.pos += mov
    
    if(keys[pg.K_UP]):
        singleEntities.append(Bullet(cam.pos, Vector2(.1,.1), '#0061c2'))


renderMethod = 0
def gameRender(wn: pg.Surface, dt: float):
    InputActions(wn, dt)
    
    wn.fill('#30a4fc')
    ground.Render()
    
    if(renderMethod == 0):
        cam.RenderLines()
    else:
        cam.RenderMatrix()
        
    ppu = 12
    mmap = pg.Surface(((minimap[1].x-minimap[0].x)*ppu, (minimap[0].y-minimap[1].y)*ppu))
    mmap.fill(groundColor)
    for l in map1:
        b = l.b*ppu
        e = l.e*ppu
        drawLine(mmap, b, e, '#ff1f1f', ppu//2)
    drawCircle(mmap, cam.pos*ppu, selectedBrawler.r*ppu, '#00a8d6')
    dmmap = 30
    wn.blit(mmap, (wn.get_width()-dmmap-mmap.get_width(), dmmap))
    
    crosshair.Render()
    pg.display.update()




benchmark = 0
class Game:
    def __init__(self, wx, wy, title):
        print("Initialazing game...")
        self.wx = wx
        self.wy = wy
        self.title = title
        self.lastTime = time.time()
        self.deltaTime = 0.1
        pg.init()
        self.wn = pg.display.set_mode((wx, wy))
        pg.display.set_caption(title)
        renderInit(self.wn)
        print("Initialization completed!")
        
    def Update(self) -> bool:    #returns False if game is exited this frame, True otherwise
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.Exit()
                return False
            
        gameRender(self.wn, self.deltaTime)
            
        self.deltaTime = time.time() - self.lastTime
        #if(benchmark != 0): print(f"deltaTime: {round(self.deltaTime, 5)}ms")
        self.lastTime = time.time()
        pg.display.set_caption(str(f"{round(1/self.deltaTime, 3)}fps"))
        return True
        
    def Exit(self):
        pg.quit()