import math

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
