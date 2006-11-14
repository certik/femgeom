class geometry(object):
    def __init__(self):
        self.d0={}
        self.d1={}
        self.d2={}
        self.d3={}
        self.phys3={}
    def add0(self,o):
        o.geom=self
        self.d0[o.getn()]=o
    def add1(self,o):
        o.geom=self
        self.d1[o.getn()]=o
    def add2(self,o):
        o.geom=self
        self.d2[o.getn()]=o
    def add3(self,o):
        o.geom=self
        self.d3[o.getn()]=o
    def addphys3(self,o):
        self.phys3[o.getn()]=o

class geomobject(object):
    def getn(self):
        return self.data[0]
    def __repr__(self):
        return str(type(self))[18]+repr(self.data[1:])

class point(geomobject):
    def __init__(self,n,p1,p2,p3):
        self.data=(n,p1,p2,p3)
    def getxyz(self):
        return self.data[1:]
    def getn(self):
        return self.data[0]
    def getstr(self):
        return "%f, %f, %f"%self.getxyz()

class line(geomobject):
    def __init__(self,n,p1,p2):
        self.data=(n,)
        self.n=n
        self.points=p1,p2
    def getpoints(self):
        return [self.geom.d0[x] for x in self.points]
    def reverse(self):
        l= line(-self.n,self.points[1],self.points[0])
        l.geom=self.geom
        return l

class lineloop(geomobject):
    def __init__(self,n,lines):
        self.data=(n,lines)
    def getlines(self):
        s=[]
        for x in self.data[1]:
            if x>0: s.append(self.geom.d1[x])
            else: s.append(self.geom.d1[-x].reverse())
        return s

class circle(geomobject):
    def __init__(self,n,p1,p2,p3):
        self.data=(n,)
        self.n=n
        self.points=p1,p2,p3
    def getpoints(self):
        return [self.geom.d0[x] for x in self.points]
    def reverse(self):
        c= circle(-self.n,self.points[2],self.points[1],self.points[0])
        c.geom=self.geom
        return c

class planesurface(geomobject):
    def __init__(self,n,boundary):
        self.data=(n,)
        self.boundary=boundary
    def getlines(self):
        #this doesn't work for negative
        return self.geom.d1[self.boundary].getlines()
    def getpoints(self):
        lines=self.getlines()
        return [x.getpoints()[0] for x in lines]

class ruledsurface(geomobject):
    def __init__(self,n,boundary):
        self.data=(n,)
        self.boundary=boundary
    def getlines(self):
        #this doesn't work for negative
        return self.geom.d1[self.boundary].getlines()
    def getpoints(self):
        lines=self.getlines()
        return [x.getpoints()[0] for x in lines]

class surfaceloop(geomobject):
    def __init__(self,n,surfaces):
        self.data=(n,surfaces)
        self.surfaces=surfaces
    def getsurfaces(self):
        s=[]
        for x in self.surfaces:
            if x>0: s.append(self.geom.d2[x])
            else: s.append(self.geom.d2[-x]) #we should actually reverse it
        return s

class volume(geomobject):
    def __init__(self,n,boundary):
        self.data=(n,boundary)
        self.boundary=boundary
    def getsurfaces(self):
        return self.geom.d2[self.boundary].getsurfaces()

class physvolume(geomobject):
    def __init__(self,n,volumes):
        self.data=(n,volumes)
        self.volumes=volumes
    def getvolumes(self):
        s=[]
        for x in self.volumes:
            if x>0: s.append(self.geom.d3[x])
            else: raise "negative volume ID"
        return s
