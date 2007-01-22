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
tC = 0.050;     //electrode (conductor) thicnkess [um]
tC = 1;     //electrode (conductor) thicnkess [um]
tI = 0.500;    //insulator (top) thickness [um]
//tI = 1.800;    //insulator (top) thickness [um]
D = G*10;       //dimension of the "system" cube [um]
tIs = D/2;      //insulator (substrate) thickness [um]
tEl = D/2;      //electrolyte thickness [um]

// program defining geometry

// substrate

p1 = newp; Point(p1) = {-D/2,-D/2,0,lc};
p2 = newp; Point(p2) = {-D/2,+D/2,0,lc};
p3 = newp; Point(p3) = {+D/2,+D/2,0,lc};
p4 = newp; Point(p4) = {+D/2,-D/2,0,lc};

l1 = newl; Line(l1) = {p1,p2};
l2 = newl; Line(l2) = {p2,p3};
l3 = newl; Line(l3) = {p3,p4};
l4 = newl; Line(l4) = {p4,p1};

ll1 = newl; Line Loop(ll1) = {l1,l2,l3,l4}; // outer line loop

Plane Surface(1) = {ll1};


// insulator

//iC=tC;
iC=0;

//p1 = newp; Point(p1) = {-D/2,-D/2,iC,lc};
//p2 = newp; Point(p2) = {-D/2,+D/2,iC,lc};
//p3 = newp; Point(p3) = {+D/2,+D/2,iC,lc};
//p4 = newp; Point(p4) = {+D/2,-D/2,iC,lc};


//hole

p1 = newp; Point(p1) = {-L/2,-W/2,iC,lc};
p2 = newp; Point(p2) = {-L/2,+W/2,iC,lc};
p3 = newp; Point(p3) = {+L/2,+W/2,iC,lc};
p4 = newp; Point(p4) = {+L/2,-W/2,iC,lc};

l1 = newl; Line(l1) = {p1,p2};
l2 = newl; Line(l2) = {p2,p3};
l3 = newl; Line(l3) = {p3,p4};
l4 = newl; Line(l4) = {p4,p1};

ll2 = newl; Line Loop(ll2) = {l1,l2,l3,l4}; // opening line loop

Plane Surface(2) = {ll1,ll2};

insulator_tmp[] = Extrude {0,0,tI+tC} {Surface{2};};

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

//volC = newv; Physical Volume(volC) = {electrodel[1], electroder[1]};

//insulator exactly
//manually obtained (gmesh:add/new/volume) surface loops defining insulator "block" with hole (insulator_tmp) and electrode volumes

Surface Loop(95) = {27,-2,23,52,31,35,39,43,47,51};
Surface Loop(96) = {94,85,-4,89,93};
Surface Loop(97) = {73,64,-3,68,72};

insulator=newv;
Volume(insulator) = {95,96,97};

//Physical Volume(1) = {insulator};

//electrolyte exactly
//manually obtained (gmesh:add/new/volume) surface loop defining electrolyte "block"

electrolyte_tmp[] = Extrude {0,0,D/2} {Surface{1};};
Surface Loop(143) = {120,107,-1,111,115,119};

electrolyte = newv;
Volume(electrolyte) = {143,95,96,97};

Physical Volume(4) = {electrolyte};

//extrude substrate

substrate[] = Extrude {0,0,-D/2} {Surface{1};};

Physical Volume(5) = {substrate[1]};

Physical Surface(1) = {94};

//finally delete tmp volumes

Delete {Volume{insulator_tmp[1]}; Volume{electrolyte_tmp[1]};}
