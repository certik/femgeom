import math

import meshutils
import geometry as geom

def numlist2str(x):
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
        assert isinstance(x,geom.surface)
        p=[map[y.getn()] for y in x.getpoints()]
        facets.append(p)
    s+="\n%d 0\n"%len(facets)
    for x in facets:
        s+="%d %s\n"%(len(x),numlist2str(x))

    #holes
    s+="\n0\n"

    #regions
    regions=[]
    for x in g.phys3.values():
        assert isinstance(x,geom.physicalvolume)
        for v in x.getvolumes():
            regions.append(v.getinsidepoint()+[x.getn()])
    s+="\n%d\n"%len(regions)
    for i,x in enumerate(regions):
        s+="%d %f %f %f %d\n"%(i,x[0],x[1],x[2],x[3])
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
        if nattrib!=1:
            raise "tetgen didn't assign an entity number to each element \
(option -A)"
        els=[]
        for line in f:
            if line[0]=="#": continue
            l=[float(x) for x in line.split()]
            assert len(l)==6
            l[0]=int(l[0])
            els.append((l[0],54,l[1],l[2],l[3],l[4]))
            if l[5]==0:
                raise "there are elements not belonging to any physical entity"
            print l[5]
            assert l[0]==len(els)
        return els
    m.nodes=getnodes(fname+".node")
    m.elements=getele(fname+".ele")
    m.is2d=False;


