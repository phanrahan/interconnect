from .. import Switch

class ConnectionBox:
    def __init__(self, inputs, tracks):
        self.switches = [Switch(tracks, inputs[i]) for i in range(len(inputs))]

    def connect(self, track, input):
        self.switch[input].connect(track, input)

    def is_connected(self, track, input):
        return self.switch[input].is_connected(track, input)

    def is_connectable(self, track, input):
        return True


