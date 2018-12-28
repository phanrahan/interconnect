import interconnect.regular as r

def test_regular():
    cgra = r.Regular(r.Core, 1, 1, 3,3)
    assert cgra.size() == (3,3)
    assert len(list(cgra.get_input(0,0,0).connections())) == 1
    #assert len(list(cgra.get_output(1,1,0).wire.ports)) == 8
    #assert len(list(cgra.get_output(1,1,0).connections())) == 8
    #assert cgra.is_connectable(1,1,0, 0,0,0)
