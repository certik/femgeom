import math

import geometry as geom

from meshutils import mesh,bound

def numlist2str(x):
    s=""
    for i in x:
        s+="%d "%i
    return s[:-1]

def getinsidepoint(pts):
    return (pts[0]+pts[1]+pts[2])/3

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
        h=[]
        pts=[]
        for hole in x.getholepoints():
            h.append([map[y.getn()] for y in hole])
            pts.append(getinsidepoint(hole).getxyz())
        bc=g.getBCnum(x.getn())
        facets.append((p,bc,h,pts))
    # # of facets, boundary markers=yes
    s+="\n%d 1\n"%len(facets)
    for p,bc,h,holes in facets:
        # # of polygons, # of holes, boundary marker
        s+="%d %d %d\n"%(1+len(h),len(h),bc)
        # # of corners, corner 1, corner 2, ...
        s+="%d %s\n"%(len(p),numlist2str(p))
        for x in h:
            # # of corners, corner 1, corner 2, ...
            s+="%d %s\n"%(len(x),numlist2str(x))
        for i,pt in enumerate(holes):
            # hole #, x, y, z
            s+="%d %f %f %f\n"%(i+1,pt[0],pt[1],pt[2])

    #volume holes
    s+="\n0\n"

    #regions
    regions=[]
    for x in g.phys3.values():
        assert isinstance(x,geom.physicalvolume)
        for v in x.getvolumes():
            regions.append(v.getinsidepoint().getxyz()+[x.getn()])
    s+="\n%d\n"%len(regions)
    for i,x in enumerate(regions):
        s+="%d %f %f %f %d\n"%(i+1,x[0],x[1],x[2],x[3])
    open(filename,"w").write(s)

def read_tetgen(fname):
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
        regions={}
        for line in f:
            if line[0]=="#": continue
            l=[int(x) for x in line.split()]
            assert len(l)==6
            els.append((l[0],54,l[1],l[2],l[3],l[4]))
            regionnum=l[5]
            if regionnum==0:
                raise "there are elements not belonging to any physical entity"
            if regions.has_key(regionnum):
                regions[regionnum].append(l[0])
            else:
                regions[regionnum]=[l[0]]
            assert l[0]==len(els)
        return els,regions
    def getBCfaces(ffaces):
        f=file(ffaces)
        l=[int(x) for x in f.readline().split()]
        nfaces,nattrib=l
        if nattrib!=1:
            raise "tetgen didn't assign an entity number to each face \
(option -A)"
        faces={}
        for line in f:
            if line[0]=="#": continue
            l=[int(x) for x in line.split()]
            assert len(l)==5
            regionnum=l[4]
            if regionnum==0: continue
            if faces.has_key(regionnum):
                faces[regionnum].append((l[1],l[2],l[3]))
            else:
                faces[regionnum]=[(l[1],l[2],l[3])]
        return faces

    m=mesh()
    b=bound()
    m.nodes=getnodes(fname+".node")
    m.elements,m.regions=getele(fname+".ele")
    m.faces=getBCfaces(fname+".face")
    return m,b