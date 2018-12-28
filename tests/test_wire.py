import interconnect as i

def test_wire():
    x = i.Port()
    y = i.Port()
    z = i.Port()
    i.connect(x, y)
    assert i.is_connected(x,y)
    assert not i.is_connected(x,z)
    assert x.get_connection()
    assert len(list(x.connections())) == 1
    assert y.get_connection()
    assert len(list(y.connections())) == 1
    i.connect(x, z)
    assert i.is_connected(x,y)
    assert i.is_connected(x,z)
    assert i.is_connected(y,z)
    assert len(list(x.connections())) == 2
    assert len(list(y.connections())) == 2
    assert len(list(z.connections())) == 2
