#! /usr/bin/env python

import sys
sys.path.append("..")
import os

import pexpect

import geom
from geom.meshutils import mesh

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
geom.write_tetgen(g,"/tmp/t.smesh")
tetgen("/home/ondra/fzu/mesh/tetgen","/tmp/t.smesh")

m=mesh()
geom.read_tetgen(m,"/tmp/t.1")
m.writemsh("/tmp/t12.msh")
m.writexda("/tmp/in.xda")
