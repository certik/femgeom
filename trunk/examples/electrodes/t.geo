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
