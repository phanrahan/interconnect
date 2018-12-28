class Port:
    def __init__(self, inst=None):
        self.inst = inst
        self.wire = None

    def get_connection(self):
        if not self.wire:
             return None
        assert len(self.wire.ports) == 2
        for port in self.wire.ports:
            if port != self:
                return port

    def connections(self):
        if not self.wire:
             return None
        for port in self.wire.ports:
            if port != self:
                yield port

