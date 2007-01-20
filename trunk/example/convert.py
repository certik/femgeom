#! /usr/bin/env python

import sys
sys.path.append("..")
import os

import pexpect

import geom
from geom.meshutils import mesh

pexpect.run("gmsh -0 t.geo -o /tmp/x.geo")
g=geom.read_gmsh("/tmp/x.geo")
geom.write_tetgen(g,"/tmp/t.smesh")
pexpect.run("/home/ondra/fzu/mesh/tetgen -pq -a0.01 /tmp/t.smesh")

m=mesh()
geom.read_tetgen(m,"/tmp/t.1")
m.writemsh("/tmp/t12.msh")
m.writexda("/tmp/in.xda")
