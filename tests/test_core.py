import interconnect as i

def test_core():
    c = i.Core(2,1)
    assert len(c.inputs) == 2
    assert len(c.outputs) == 1
