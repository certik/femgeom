import math

import meshutils
import geometry as geom

def conv(x):
    s=""
    for i in x:
        s+="%d "%i
    return s[:-1]

def write_tetgen(g,filename):
    #nodes
    nodes=[]
    map={}
    for x in g.d0.values():
        assert isinstance(x,geom.point)
        nodes.append(x.getxyz())
        map[x.getn()]=len(nodes)
    s="%d 3\n"%len(nodes)
    for n,x in enumerate(nodes):
        s+="%d %f %f %f\n"%tuple([n+1]+list(x))

    #facets
    facets=[]
    for x in g.d2.values():
        if isinstance(x,geom.planesurface) or isinstance(x,geom.ruledsurface):
            p=[map[y.getn()] for y in x.getpoints()]
            facets.append(p)
        elif isinstance(x,geom.surfaceloop):
            continue
        else:
            print "Warning: unknown element ",type(x)
            continue
    s+="\n%d 0\n"%len(facets)
    for x in facets:
        s+="%d %s\n"%(len(x),conv(x))

    #holes
    s+="\n0\n"
    #regions
    s+="\n0\n"
    open(filename,"w").write(s)

def read_tetgen(m,fname):
    def getnodes(fnods):
        f=file(fnods)
        l=[int(x) for x in f.readline().split()]
        npoints,dim,nattrib,nbound=l
        assert dim==3
        nodes=[]
        for line in f:
            if line[0]=="#": continue
            l=[float(x) for x in line.split()]
            l[0]=int(l[0])
            nodes.append(tuple(l))
            assert l[0]==len(nodes)
        assert npoints==len(nodes)
        return nodes
    def getele(fele):
        f=file(fele)
        l=[int(x) for x in f.readline().split()]
        ntetra,nnod,nattrib=l
        assert nnod==4
        els=[]
        for line in f:
            if line[0]=="#": continue
            l=[float(x) for x in line.split()]
            l[0]=int(l[0])
            els.append((l[0],54,l[1],l[2],l[3],l[4]))
            assert l[0]==len(els)
        return els
    m.nodes=getnodes(fname+".node")
    m.elements=getele(fname+".ele")
    m.is2d=False;


