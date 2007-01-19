#! /usr/bin/env python

import sys
sys.path.append("..")
import os

import geom
from geom.meshutils import mesh

os.system("gmsh -0 t.geo -o /tmp/x.geo -v 0")
g=geom.read_gmsh("/tmp/x.geo")
geom.write_tetgen(g,"/tmp/t.smesh")
os.system("~/fzu/mesh/tetgen -pqQ -a0.01 /tmp/t.smesh")

m=mesh()
geom.read_tetgen(m,"/tmp/t.1")
m.writemsh("/tmp/t12.msh")
m.writexda("/tmp/in.xda")
