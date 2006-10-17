"""
Polygon partitioning and other utilities.

It's simple, it's in pure python and it just works, although the algorithm is
not the fastest (but for polygons with 5 or 10 vertices it doesn't matter
anyway).

Usage:

>>> import poly 
>>> poly.triangulate([(0,0), (1,0), (0,1), (0.5, 0.25)])
[[(1, 0), (0, 1), (0.5, 0.25)], [(0, 0), (1, 0), (0.5, 0.25)]]


Note: This algorithm is a home-made hybrid, better is to use "ear clipping"
algorithm, but I didn't know about it when I wrote this.

"""

def isright(a,b,c):
    "is c on the right, or on the left of the arrow a-->b?"
    return (b[0]-a[0])*(c[1]-a[1])<(b[1]-a[1])*(c[0]-a[0])

def isline(t):
    a=t[0]
    b=t[1]
    c=t[2]
    return abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))<1e-6

def convex(vertices):
    vertices=vertices+[vertices[0]]
    dir=isright(vertices[0],vertices[1],vertices[2])
    for i in range(1,len(vertices)-2):
        if isright(vertices[i],vertices[i+1],vertices[i+2])!=dir:
            return False
    return True

def isinpolygon(x,vertices):
    if x in vertices: return False
    isin=False
    vj=vertices[-1]
    for vi in vertices:
        if ((vi[1]<=x[1] and x[1]<vj[1]) or (vj[1]<=x[1] and x[1]<vi[1])) and \
            (x[0] < (vj[0]-vi[0])*(x[1]-vi[1])/(vj[1]-vi[1]) + vi[0]):
            isin=not isin;
        vj=vi
    return isin;

def overlapping(pol1,pol2):
    for x in pol1:
        if isinpolygon(x,pol2):
            return True
    for x in pol2:
        if isinpolygon(x,pol1):
            return True
    return False

def triangulate(vertices):
    if len(vertices)==3:
        if isline(vertices):
            return []
        else:
            return [vertices]
    elif convex(vertices):
        r=[]
        for i in range(2,len(vertices)):
            v=[vertices[0]]+vertices[i-1:i+1]
            if not isline(v):
                r.append(v)
        return r
    else:
        n1=0
        n2=n1+2
        pol1=vertices[n1:n2+1]
        pol2=vertices[:n1+1]+vertices[n2:]
#        print pol1, pol2
        while overlapping(pol1,pol2):
            if n2<len(vertices)-2:
                n2+=1
            elif n1<len(vertices)-3:
                n1+=1
                n2=n1+2
            else:
                raise "didn't find any partitioning"
            pol1=vertices[n1:n2+1]
            pol2=vertices[:n1+1]+vertices[n2:]
#            print pol1, pol2
        return triangulate(pol1)+triangulate(pol2)
