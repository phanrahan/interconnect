import interconnect as i

def test_switch():
    s = i.Switch(2,1)
    x = s.inputs[0]
    y = s.inputs[1]
    z = s.outputs[0]
    i.connect(x,y)
    assert i.is_connected(x,y)
    assert not i.is_connected(x,z)
