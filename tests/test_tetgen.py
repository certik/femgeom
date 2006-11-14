import sys
sys.path.append(".")

import geom

def test1():
    open("/tmp/t2.geo","w").write("""\
    Point(1) = {0.1, 0.1, 0, 0.1};
    Point(2) = {0.6, 0.1, 0, 0.1};
    Point(3) = {0.6, 0.6, 0, 0.1};
    Point(4) = {0.1, 0.6, 0, 0.1};
    Point(6) = {0.1, 0.6, -0.5, 0.1};
    Point(7) = {0.1, -0, -0.5, 0.1};
    Point(8) = {-0.9, 0.6, -0.5, 0.1};
    Point(9) = {-0.9, 0, -0.5, 0.1};
    Point(13) = {-0.9, 0.1, 0, 0.1};
    Point(17) = {-0.9, 0.6, 0, 0.1};
    Line (1) = {3, 4};
    Line (2) = {4, 1};
    Line (3) = {1, 2};
    Line (4) = {2, 3};
    Line (7) = {6, 3};
    Line (8) = {6, 7};
    Line (9) = {2, 7};
    Line (10) = {1, 7};
    Line (11) = {4, 6};
    Line (25) = {8, 9};
    Line (26) = {9, 13};
    Line (27) = {13, 17};
    Line (28) = {17, 8};
    Line (30) = {6, 8};
    Line (31) = {7, 9};
    Line (35) = {1, 13};
    Line (39) = {4, 17};
    Line Loop (1000013) = {8, -10, -2, 11};
    Plane Surface (13) = {1000013};
    Line Loop (1000015) = {7, 1, 11};
    Plane Surface (15) = {1000015};
    Line Loop (1000017) = {9, -10, 3};
    Plane Surface (17) = {1000017};
    Line Loop (1000019) = {8, -9, 4, -7};
    Plane Surface (19) = {1000019};
    Line Loop (1000021) = {1, 2, 3, 4};
    Plane Surface (21) = {1000021};
    Line Loop (1000032) = {8, 31, -25, -30};
    Ruled Surface (32) = {1000032};
    Line Loop (1000036) = {-10, 35, -26, -31};
    Ruled Surface (36) = {1000036};
    Line Loop (1000040) = {-2, 39, -27, -35};
    Ruled Surface (40) = {1000040};
    Line Loop (1000044) = {11, 30, -28, -39};
    Ruled Surface (44) = {1000044};
    Line Loop (1000045) = {25, 26, 27, 28};
    Plane Surface (45) = {1000045};
    Surface Loop (1000023) = {19, 13, 17, 21, 15};
    Volume (23) = {1000023};
    Surface Loop(1000046) = {44,-13,32,36,40,45};
    Volume(24) = {1000046};
    Physical Volume(100)={23,24};
""")

    g=geom.read_gmsh("/tmp/t2.geo")
    geom.write_tetgen(g,"/tmp/t2.smesh")
