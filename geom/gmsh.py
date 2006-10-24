import math

from pyparsing import Word, Optional, alphas, nums, Combine, Literal, \
CaselessLiteral, LineEnd, Group, Dict, OneOrMore, StringEnd, restOfLine, \
ParseException, oneOf, Forward, alphanums, Keyword, SkipTo

import geom


def read_gmsh(filename):

    e = CaselessLiteral("E")
    inum = Word("+-"+nums)
    fnum = Combine( 
        Word( "+-"+nums, nums ) + Optional("."+Optional(Word(nums))) +
        Optional(e+Word("+-"+nums,nums)) 
        )

    semi  = Literal(";").suppress()
    colon  = Literal(",").suppress()
    lpar  = Literal("(").suppress()
    rpar  = Literal(")").suppress()
    lbrace  = Literal("{").suppress()
    rbrace  = Literal("}").suppress()
    eq  = Literal("=").suppress()

    point = Group(
            Keyword("Point")+lpar+inum+rpar+eq+
            Group(lbrace+fnum+colon+fnum+colon+fnum+colon+fnum+rbrace)+semi
            )
    line = Group(
            Keyword("Line")+lpar+inum+rpar+eq+
            Group(lbrace+inum+colon+inum+rbrace)+semi
            )
    lineloop = Group(
            Keyword("Line Loop")+lpar+inum+rpar+eq+
            Group(lbrace+inum+OneOrMore(colon+inum)+rbrace)+semi
            )
    circle = Group(
            Keyword("Circle")+lpar+inum+rpar+eq+
            Group(lbrace+inum+colon+inum+colon+inum+rbrace)+semi
            )
    planesurface = Group(
            Keyword("Plane Surface")+lpar+inum+rpar+eq+
            Group(lbrace+inum+rbrace)+semi
            )
    ruledsurface = Group(
            Keyword("Ruled Surface")+lpar+inum+rpar+eq+
            Group(lbrace+inum+rbrace)+semi
            )
    surfaceloop = Group(
            Keyword("Surface Loop")+lpar+inum+rpar+eq+
            Group(lbrace+inum+OneOrMore(colon+inum)+rbrace)+semi
            )
    volume = Group(
            Keyword("Volume")+lpar+inum+rpar+eq+
            Group(lbrace+inum+rbrace)+semi
            )
    physicalvolume = Group(
            Keyword("Physical Volume")+lpar+inum+rpar+eq+
            Group(lbrace+inum+OneOrMore(colon+inum)+rbrace)+semi
            )

    comment = Group( Literal("//")+restOfLine).suppress()

    command = point | line | lineloop | circle | planesurface | ruledsurface | \
            surfaceloop | volume | physicalvolume | comment

    grammar= OneOrMore(command)+StringEnd()

    try:
        tokens= grammar.parseFile(filename)
    except ParseException, err:
        print err.line
        print " "*(err.column-1) + "^"
        print err
        raise err

    g=geom.geometry()
    for x in tokens:
        if x[0]=="Point":
            g.add0(geom.point(int(x[1]),float(x[2][0]),float(x[2][1]),
                float(x[2][2])))

        elif x[0]=="Line":
            assert len(x[2])==2
            g.add1(geom.line(int(x[1]),int(x[2][0]),int(x[2][1])))
        elif x[0]=="Circle":
            assert len(x[2])==3
            g.add1(geom.circle(int(x[1]),int(x[2][0]),int(x[2][1]),
                int(x[2][2])))
        elif x[0]=="Line Loop":
            g.add1(geom.lineloop(int(x[1]),[int(y) for y in x[2]]))

        elif x[0]=="Plane Surface":
            assert len(x[2])==1
            g.add2(geom.planesurface(int(x[1]),int(x[2][0])))
        elif x[0]=="Ruled Surface":
            assert len(x[2])==1
            g.add2(geom.ruledsurface(int(x[1]),int(x[2][0])))
        elif x[0]=="Surface Loop":
            g.add2(geom.surfaceloop(int(x[1]),[int(y) for y in x[2]]))

        elif x[0]=="Volume":
            assert len(x[2])==1
            g.add3(geom.volume(int(x[1]),int(x[2][0])))
        elif x[0]=="Physical Volume":
            pass
        else:
            raise "Unsupported entity: "+x[0]
    return g
