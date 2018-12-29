brom .. import Switch

class SwitchBox:
    def __init__(self, num_tracks: int, num_inputs: int):
        self.num_tracks = num_tracks
        self.num_inputs = num_inputs

        # create switches
        self.switches = 4 * [None]
        for side in range(4):
            self.switches[side] = num_tracks * [None]
            for track in range(num_tracks):
                self.switches[side][track] = Switch(4, 1)

        # create input Port per side per track
        # connect inputs to switches
        self.inputs = 4 * [None]

        # create output Port per side per track
        # connect outputs of switches to ports
        self.outputs = 4 * [None]

    def num_switches(self) -> int:
        return 4*self.num_tracks

    def inside(self, side, track) -> bool:
        if not (0 <= track < self.num_tracks):
            raise ValueError(f"Invalid track {track}")
            return False
        return True

    def get_switch(self, side : Side, track : int) -> Switch:
        self.inside(side, track)
        return self.switches[side][track]

    def get_input(self, side : Side, track : int) -> Switch:
        self.inside(side, track)
        return self.switches[side][track].get_input(track)

    def get_output(self, side : Side, track : int) -> Switch:
        self.inside(side, track)
        return self.switches[side][track].get_output(0)


    def is_connectable(self,
                     side0 : Side,
                     track0 : int,
                     side1 : Side,
                     track1 : int) -> bool:
        self.inside(side0, track0)
        self.inside(side1, track1)
        return side0 != side1 and track0 == track1

    def connect(self,
                     side0 : Side,
                     track0 : int,
                     side1 : Side,
                     track1 : int) -> bool:
        self.inside(side0, track0)
        self.inside(side1, track1)
        raise NotImplemented(f"SwitchBox.connect}")

    def is_connected(self,
                     side0 : Side,
                     track0 : int,
                     side1 : Side,
                     track1 : int) -> bool:
        self.inside(side0, track0)
        self.inside(side1, track1)
        raise NotImplemented(f"SwitchBox.is_connected}")

