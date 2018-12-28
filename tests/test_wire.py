import interconnect as i

def test_wire():
    x = i.Port()
    y = i.Port()
    z = i.Port()
    i.connect(x, y)
    assert i.is_connected(x,y)
    assert not i.is_connected(x,z)
