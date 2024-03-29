#! /usr/bin/env python

import sys
sys.path.append("../..")

import pexpect

import geom

pexpect.run("gmsh -0 t.geo -o /tmp/x.geo")
g=geom.read_gmsh("/tmp/x.geo")
g.printinfo()
geom.write_tetgen(g,"/tmp/t.poly")

print "Generating mesh using tetgen..."
geom.runtetgen("/home/ondra/fzu/mesh/tetgen","/tmp/t.poly")

print "Reading mesh from tetgen..."
m=geom.read_tetgen("/tmp/t.1")
m.writemsh("/tmp/t12.msh")
print "Mesh written to /tmp/t12.msh"
m.writexda("/tmp/in.xda")
print "Mesh written to /tmp/in.xda"
m.writeregions("/tmp/t12.regions")
print "Regions written to /tmp/t12.regions"
m.writeBC("/tmp/t12.boundaries")
print "Boundaries written to /tmp/t12.boundaries"
