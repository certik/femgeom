"""
Polygon partitioning and other utilities.

It's simple, it's in pure python and it just works, although the algorithm is
not the fastest (but for polygons with 5 or 10 vertices it doesn't matter
anyway).

Usage:

>>> import poly 
>>> poly.triangulate([(0,0), (1,0), (0,1), (0.5, 0.25)])
[[(1, 0), (0, 1), (0.5, 0.25)], [(0, 0), (1, 0), (0.5, 0.25)]]

"""
from poly import triangulate, isright, convex, isinpolygon, overlapping

def test3():
    assert triangulate([(0,0), (1,0), (0,1)]) == [[(0,0), (1,0), (0,1)]]

def test4convex():
    assert triangulate([(0,0), (1,0), (1,1), (0,1)]) == [
            [(0,0), (1,0), (1,1)],
            [(0,0), (1,0), (0,1)],
            ]
    assert triangulate([(0,0), (1,0), (1,1), (0,1)]) != [
            [(0,0), (1,0), (1,1)],
            [(0,0), (1,0), (1,1)],
            ]

def test4concave():
    assert triangulate([(0,0), (1,0), (0,1), (0.5, 0.25)]) != [
            [(0, 0), (1, 0), (0, 1)], 
            [(0, 0), (1, 0), (0.5, 0.25)]
            ]
    assert triangulate([(0,0), (1,0), (0,1), (0.5, 0.25)]) == [
            [(1, 0), (0, 1), (0.5, 0.25)],
            [(0, 0), (1, 0), (0.5, 0.25)]
            ]

    assert triangulate([(0,0), (0.5, 0.25), (0,1), (1,0)]) == [
            [(0.5, 0.25), (0,1), (1,0)],
            [(0, 0), (0.5, 0.25), (1,0)]
            ]

def testisright():
    assert isright((0,0), (0,1), (1,1))
    assert not isright((0,0), (0,1), (-1,1))
    assert isright((0,0), (1,0), (1,-1))
    assert not isright((0,0), (1,0), (1,1))

def testconvex():
    assert convex([ (0,0), (1,0), (1,1) ])

    assert convex([ (0,0), (1,0), (1,1), (0,1) ])
    assert not convex([ (0,0), (1,0), (0,1), (0.5, 0.25) ])

def testisin():
    assert not isinpolygon((-1,0),[(0,0), (0.5, 0.25), (0,1), (1,0)])
    assert isinpolygon((0.5,0.2),[(0,0), (0.5, 0.25), (0,1), (1,0)])
    assert isinpolygon((0.51,0.25),[(0,0), (0.5, 0.25), (0,1), (1,0)])
    assert not isinpolygon((0.49,0.25),[(0,0), (0.5, 0.25), (0,1), (1,0)])
    assert isinpolygon((0.49,0.25),[(0,0), (0,1), (1,0)])

def testoverlapping():
    assert not overlapping([(0, 0), (1, 0), (0.5, 0.25)],
            [(1, 0), (0, 1), (0.5, 0.25)])
