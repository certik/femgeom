/*
Gmsh model of a nanocyrstalline silicon film.

2007 Ondrej Certik
*/

Point(1) = {0, 1.0, 0, 0.1};
Point(2) = {0, 0, 0, 0.1};
Point(3) = {1.8, 0, 0, 0.1};
Point(4) = {1.8, 1.0, 0, 0.1};
Point(5) = {0.5, 1.0, 0, 0.1};
Point(6) = {0.4, 0.8, 0, 0.1};
Point(7) = {0.3, 0.6, 0, 0.1};
Point(8) = {0.2, 0.4, 0, 0.1};
Point(9) = {0.1, 0.2, 0, 0.1};
Point(10) = {0, 0.1, 0, 0.1};

Line(1) = {2,3};
Line(2) = {3,4};
Line(3) = {4,5};
Line(4) = {5,1};
Line(5) = {1,10};
Line(6) = {10,2};
Line(7) = {10,9};
Line(8) = {9,8};
Line(9) = {8,7};
Line(10) = {7,6};
Line(11) = {6,5};
Line Loop(12) = {3,-11,-10,-9,-8,-7,6,1,2};
Plane Surface(13) = {12};
Line Loop(14) = {4,5,7,8,9,10,11};
Plane Surface(15) = {14};
Extrude {{0,1,0}, {-0.9+0.9,0,0}, Pi/4} {
  Surface{13,15};
}
Extrude {{0,1,0}, {-0.9+0.9,0,0}, Pi/4} {
  Surface{57,89};
}
Extrude {{0,1,0}, {-0.9+0.9,0,0}, Pi/4} {
  Surface{131,163};
}
Extrude {{0,1,0}, {-0.9+0.9,0,0}, Pi/4} {
  Surface{237,205};
}
Extrude {{0,1,0}, {-0.9+0.9,0,0}, Pi/4} {
  Surface{311,269};
}
Extrude {{0,1,0}, {-0.9+0.9,0,0}, Pi/4} {
  Surface{385,353};
}
Extrude {{0,1,0}, {-0.9+0.9,0,0}, Pi/4} {
  Surface{417,459};
}
Extrude {{0,1,0}, {-0.9+0.9,0,0}, Pi/4} {
  Surface{491,533};
}
Surface Loop(606) = {177,103,29,578,505,431,325,283,-268,181,107,33,-564,-490,-416,329,333,-264,185,111,37,-560,-486,-412,-408,337,-260,189,115,41,-556,-482,-478,-404,341,-256,193,119,45,-552,-548,-474,-400,344,-252,196,122,48,310,204,130,56,605,532,458,352,348,306,200,126,52,601,528,454};
Volume(607) = {606};
Surface Loop(608) = {329,-268,181,107,33,-564,-490,-416,-396,-470,-544,-68,-142,-216,-248,-364,-412,333,-264,185,111,37,-560,-486,-482,-408,337,-260,189,115,41,-556,-552,-478,-404,341,-256,193,119,45,48,122,196,-252,344,-400,-474,-548};
Volume(609) = {608};

Physical Volume (100)={607,609};
