import sys
sys.path.append(".")

import geom

def test1():
    open("/tmp/t1.geo","w").write("""\
Point(1) = {0.1, 0.1, 0, 0.1};
Point(2) = {0.6, 0.1, 0, 0.1};
Point(3) = {0.6, 0.5, 0, 0.1};
Point(4) = {0.1, 0.5, 0, 0.1};
Point(6) = {0.1, 0.4, -0.5, 0.1};
Point(7) = {0.2, -0, -0.5, 0.1};
Line (1) = {3, 4};
Line (2) = {4, 1};
Line (3) = {1, 2};
Line (4) = {2, 3};
Line (7) = {6, 3};
Line (8) = {6, 7};
Line (9) = {2, 7};
Line (10) = {1, 7};
Line (11) = {4, 6};
    """);
    g=geom.read_gmsh("/tmp/t1.geo")
    geom.write_femlab(g,"/tmp/t2.m",export1D=True)
