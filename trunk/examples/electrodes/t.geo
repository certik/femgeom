/*********************************************************************
 *
 *  Gmsh model of nanoelectrode system
 *
 *  Bohuslav Rezek, 2006
 *
 *********************************************************************/

// definition of constants

lc = 1;       //defines point "size"

G = 2;          //electrode gap [um]
A = 90;         //electrode tip angle [deg]
L = G+1;        //opening length [um]
W = 1;          //opening width [um]
//tC = 0.050;     //electrode (conductor) thicnkess [um]
tC = 1;     //electrode (conductor) thicnkess [um]
tI = 0.500;    //insulator (top) thickness [um]
//tI = 1.800;    //insulator (top) thickness [um]
D = G*10;       //dimension of the "system" cube [um]
tIs = D/2;      //insulator (substrate) thickness [um]
tEl = D/2;      //electrolyte thickness [um]

// electrode left

p1 = newp; Point(p1) = {-G/2,0,0,lc}; //electrode tip

ytmp = Tan(A*Pi/180/2)*(D-G)/2;

p2 = newp; Point(p2) = {-D/2,-ytmp,0,lc};
p3 = newp; Point(p3) = {-D/2,+ytmp,0,lc};

l1 = newl; Line(l1) = {p1,p2};
l2 = newl; Line(l2) = {p2,p3};
l3 = newl; Line(l3) = {p3,p1};

ll1 = newl; Line Loop(ll1) = {l1,l2,l3};

Plane Surface(3) = {ll1};

electrodel[] = Extrude {0,0,tC} {Surface{3};};

Physical Volume(2) = {electrodel[1]};


// electrode right

p1 = newp; Point(p1) = {G/2,0,0,lc}; //electrode tip
p2 = newp; Point(p2) = {D/2,-ytmp,0,lc};
p3 = newp; Point(p3) = {D/2,+ytmp,0,lc};

l1 = newl; Line(l1) = {p1,p2};
l2 = newl; Line(l2) = {p2,p3};
l3 = newl; Line(l3) = {p3,p1};

ll1 = newl; Line Loop(ll1) = {l1,l2,l3};

Plane Surface(4) = {ll1};

electroder[] = Extrude {0,0,tC} {Surface{4};};

Physical Volume(3) = {electroder[1]};

Physical Surface(1) = {electroder[0]};

//substrate
z=0;
p1 = newp; Point(p1) = {-D/2,-D/2,z,lc};
p2 = newp; Point(p2) = {-D/2,+D/2,z,lc};
p3 = newp; Point(p3) = {+D/2,+D/2,z,lc};
p4 = newp; Point(p4) = {+D/2,-D/2,z,lc};

l2 = newl; Line(l2) = {p2,p3};
l4 = newl; Line(l4) = {p4,p1};
Line(45) = {20,3};
Line(46) = {2,19};
Line(47) = {11,22};
Line(48) = {12,21};
Line Loop(49) = {43,-48,24,22,47,44,-46,-1,-3,-45};

Plane Surface(50) = {49};
substrate[] = Extrude {0,0,-D/2} {Surface{50,3,4};};

Physical Volume(1) = {substrate[1],4,5};

/*
//hole
iC=0;

p1 = newp; Point(p1) = {-L/2,-W/2,iC,lc};
p2 = newp; Point(p2) = {-L/2,+W/2,iC,lc};
p3 = newp; Point(p3) = {+L/2,+W/2,iC,lc};
p4 = newp; Point(p4) = {+L/2,-W/2,iC,lc};

l5 = newl; Line(l5) = {p2,p3};
l6 = newl; Line(l6) = {p4,p1};

p1 = newp; Point(p1) = {-L/2,-W/2,tC,lc};
p2 = newp; Point(p2) = {-L/2,+W/2,tC,lc};
p3 = newp; Point(p3) = {+L/2,+W/2,tC,lc};
p4 = newp; Point(p4) = {+L/2,-W/2,tC,lc};
Line(139) = {57,61};
Line(140) = {61,64};
Line(141) = {64,60};
Line(142) = {62,58};
Line(143) = {62,63};
Line(144) = {63,59};

p5 = newp; Point(p5) = {-L/2,-W/2,tC+tI,lc};
p6 = newp; Point(p6) = {-L/2,+W/2,tC+tI,lc};
p7 = newp; Point(p7) = {+L/2,+W/2,tC+tI,lc};
p8 = newp; Point(p8) = {+L/2,-W/2,tC+tI,lc};
Line(145) = {61,65};
Line(146) = {65,68};
Line(147) = {68,64};
Line(148) = {65,66};
Line(149) = {66,67};
Line(150) = {67,68};
Line(151) = {67,63};
Line(152) = {66,62};
Line(153) = {63,64};
Line(154) = {62,61};

Line Loop(155) = {140,141,138,139};
Plane Surface(156) = {155};
Line Loop(157) = {137,-144,-143,142};
Plane Surface(158) = {157};
Line Loop(159) = {150,147,-153,-151};
Plane Surface(160) = {159};
Line Loop(161) = {149,151,-143,-152};
Plane Surface(162) = {161};
Line Loop(163) = {148,152,154,145};
Plane Surface(164) = {163};
Line Loop(165) = {146,147,-140,145};
Plane Surface(166) = {165};
Line Loop(167) = {149,150,-146,148};
Plane Surface(168) = {167};

//insulator

z=0;
p1 = newp; Point(p1) = {-D/2,-D/2,tC+tI,lc};
p2 = newp; Point(p2) = {-D/2,+D/2,tC+tI,lc};
p3 = newp; Point(p3) = {+D/2,+D/2,tC+tI,lc};
p4 = newp; Point(p4) = {+D/2,-D/2,tC+tI,lc};
Line(169) = {70,69};
Line(170) = {69,72};
Line(171) = {72,71};
Line(172) = {71,70};
Line(173) = {72,22};
Line(174) = {69,19};
Line(175) = {71,21};
Line(176) = {70,20};
Line Loop(177) = {28,-36,48,-175,-171,173,-47,32};
Plane Surface(178) = {177};
Line Loop(179) = {44,-174,170,173};
Plane Surface(180) = {179};
Line Loop(181) = {172,176,43,-175};
Plane Surface(182) = {181};
Line Loop(183) = {15,-7,-11,46,-174,-169,176,45};
Plane Surface(184) = {183};
Line Loop(185) = {172,169,170,171};
Plane Surface(186) = {185};
*/
