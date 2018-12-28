class Wire:
    def __init__(self):
        self.ports = set() 

    def is_connected(self, port1, port2):
        return port1 in self.ports and port2 in self.ports

    def connect( self, port1, port2):
        if port1 not in self.ports:
            self.ports.add(port1)
        if port2 not in self.ports:
            self.ports.add(port2)
        port1.wire = self
        port2.wire = self

    def merge(self, port):
        self.ports |= port.wire.ports
        port.wire = self

def connect(port1, port2):
    if port1.wire and port2.wire:
        if port1.wire is not port2.wire:
            w = Wire()
            w.merge(port1)
            w.merge(port2)
    else:
        if   port1.wire:
            w = port1.wire
        elif port2.wire:
            w = port2.wire
        else:
            w = Wire()
        w.connect(port1, port2)

def is_connected(port1, port2):
    if port1.wire is None:
        return False
    if port2.wire is None:
        return False
    if port1.wire != port2.wire:
        return False
    w = port1.wire
    return w.is_connected(port1, port2)

