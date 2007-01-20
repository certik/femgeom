class geometry(object):
    """The geometry is given by a sets of points (d0), lines (d1), surfaces
    (d2) and volumes (d3). Lines are constructed from 2 points, surface from
    any number of lines, volume from any number of surfaces.

    Physical volumes are contruted from any number of volumes.
    """
    def __init__(self):
        self.d0={}
        self.d1={}
        self.d2={}
        self.d3={}
        self.phys3={}
    def addpoint(self,n,p):
        "p=[x,y,z]"
        o=point(self,n,p)
        self.d0[o.getn()]=o
    def addline(self,n,l)
        "l=[p1,p2]"
        o=line(self,n,l)
        self.d1[o.getn()]=o
    def printinfo(self):
        print "General geometry information:"
        print "  points:",len(self.d0)
        print "  lines:",len(self.d1)
        print "  surfaces:",len(self.d2)
        print "  volumes:",len(self.d3)
        print "Physical volumes:"
        for d in self.phys3:
            print d,self.phys3[d]

class geomobject(object):
    def getn(self):
        return self.data[0]
    def __repr__(self):
        return str(type(self))[18]+repr(self.data[1:])

class point(geomobject):
    def __init__(self,g,n,p):
        self.geom=g
        self.n=n
        self.p=p
    def getxyz(self):
        return self.p
    def getn(self):
        return self.n
    def getstr(self):
        return "%f, %f, %f"%self.getxyz()

class line(geomobject):
    def __init__(self,g,n,l):
        self.geom=g
        self.n=n
        self.points=l
    def getpoints(self):
        return self.points
#    def reverse(self):
#        l= line(-self.n,self.points[1],self.points[0])
#        l.geom=self.geom
#        return l

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
