#! /usr/bin/env python

import sys
sys.path.append("..")
import os

import geom

os.system("gmsh -0 t.geo -o /tmp/x.geo -v 0")
g=geom.read_gmsh("/tmp/x.geo")
geom.write_femlab(g,"/tmp/t.m",export3D=True)

