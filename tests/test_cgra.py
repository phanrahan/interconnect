import interconnect.cgra as r

def test_regular():
    cgra = r.Planar(2, 1, 2, 3,3)
    assert cgra.size() == (3,3)
    assert cgra.is_connectable((0,0),r.Side.EAST,0, (1,0),r.Side.WEST,0)
    assert cgra.is_connectable((0,0),r.Side.EAST,0, (2,0),r.Side.WEST,0)
    assert not cgra.is_connectable((0,0),r.Side.NORTH,0, (1,0),r.Side.SOUTH,0)
    assert not cgra.is_connectable((0,0),r.Side.EAST,0, (0,1),r.Side.WEST,0)
    assert cgra.is_connectable((0,0),r.Side.NORTH,0, (0,1),r.Side.SOUTH,0)
    assert cgra.is_connectable((0,0),r.Side.NORTH,0, (0,2),r.Side.SOUTH,0)
