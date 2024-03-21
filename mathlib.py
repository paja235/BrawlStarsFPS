import math
import copy


INF = 2147483647
PI = 3.141592653
DTOR = PI/180


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __add__(self, v):
        return Vector2(self.x+v.x, self.y+v.y)
    def __sub__(self, v):
        return Vector2(self.x-v.x, self.y-v.y)
    def __mul__(self, v):
        return Vector2(self.x*v, self.y*v)
    def __truediv__(self, v):
        return Vector2(self.x/v, self.y/v)
    def __xor__(self, v):
        return self.x*v.y - self.y*v.x
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def normalize(self) -> None:
        d = math.sqrt(self.x*self.x + self.y*self.y)
        if(d==0): return
        self.x /= d
        self.y /= d
    def magnitute(self) -> float:
        return math.sqrt(self.x*self.x+self.y*self.y)
    def rotate(self, angle: float) -> None:
        x1 = self.x * math.cos(angle*DTOR) - self.y * math.sin(angle*DTOR)
        self.y = self.x * math.sin(angle*DTOR) + self.y * math.cos(angle*DTOR)
        self.x = x1
    
vzero = Vector2(0,0)
sss = Vector2(69,69)

    
class Line:
    def __init__(self, b: Vector2, e: Vector2):
        self.b = b
        self.e = e
        self.d = e-b
        self.normal = Vector2(self.d.y, -self.d.x)
        self.normal.normalize()
    def distance(self, v: Vector2, thickness: float) -> Vector2:
        ray = Ray(v, -self.normal)
        d = ray.intersect(self)
        if(d == INF):
            def dis(p: Vector2) -> Vector2:
                r = p-v
                if(r.magnitute() > thickness): return vzero
                n = copy.deepcopy(r)
                n.normalize()
                n *= thickness
                return n-r
            bd = dis(self.b)
            if(bd != vzero): return bd
            return dis(self.e)
        if(abs(d) >= thickness): return vzero
        nor = self.normal if d > 0 else -self.normal
        nor *= thickness - abs(d)
        return -nor
        
        
class Ray:
    def __init__(self, o: Vector2, d: Vector2):
        self.o = o
        self.d = d
    @classmethod
    def fromAngle(cls, o: Vector2, r: float):
        return cls(o, Vector2(math.sin(r/180*PI), math.cos(r/180*PI)))
    def intersect(self, l: Line) -> float:
        q = l.b
        s = l.d
        p = self.o
        r = self.d
        d = r^s
        if(d == 0): return INF
        m = q-p
        t = (m^s)/d
        u = (m^r)/d
        if(u <= 1 and u >= 0): return t
        return INF
    