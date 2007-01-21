#! /usr/bin/env python

#import cgitb;cgitb.enable(format="text")

import sys
sys.path.append("../..")
import os

import pexpect

import geom

def tetgen(tetgenpath,filename):
    cmd="%s -pqQA -a0.01 %s"%(tetgenpath,filename)
    p=pexpect.spawn(cmd)
    p.expect("Opening %s."%(filename))
    assert p.before==""
    p.expect(pexpect.EOF)
    if p.before!="\r\n":
        print p.before
        raise "Error when running tetgen (see above for output): %s"%cmd


pexpect.run("gmsh -0 t.geo -o /tmp/x.geo")
g=geom.read_gmsh("/tmp/x.geo")
g.printinfo()
geom.write_tetgen(g,"/tmp/t.poly")

print "Generating mesh..."
tetgen("/home/ondra/fzu/mesh/tetgen","/tmp/t.poly")

m,b=geom.read_tetgen("/tmp/t.1")
m.writemsh("/tmp/t12.msh")
print "Mesh written to /tmp/t12.msh"
m.writexda("/tmp/in.xda")
print "Mesh written to /tmp/in.xda"
m.writeregions("/tmp/t12.regions")
print "Regions written to /tmp/t12.regions"
m.writeBC("/tmp/t12.boundaries")
print "Boundaries written to /tmp/t12.boundaries"
