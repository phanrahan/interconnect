import interconnect.regular as r

def test_regular():
    cgra = r.Regular(2, 1, 3,3)
    assert cgra.size() == (3,3)
    assert cgra.is_connectable((1,1),0, (0,0),0)
    assert cgra.is_connectable((1,1),0, (1,0),0)
    assert not cgra.is_connectable((1,1),0, (1,0),1)
    assert not cgra.is_connectable((0,0),0, (2,2),0)
    #assert len(list(cgra.get_input(0,0,0).connections())) == 1
    #assert len(list(cgra.get_output(1,1,0).connections())) == 8
