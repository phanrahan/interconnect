from interconnect import *

class SwitchBox:
    def __init__(self, num_tracks : int, inputs):
        self.num_tracks = num_tracks
        for side in range(4):
            for track in range(num_tracks):
               # create switchbox per [side][track]
               # connect to other sides and inputs
               pass

    def num_switches(self) -> int:
        return 4*self.num_tracks

    def get_switch(self, side : Side, index : int) -> SwitchNode:
        if index >= self.num_tracks:
            raise ValueError(f"Invalid index {index}")
        return SwitchNode()

    def is_connected(self,
                     side0 : Side,
                     index0 : int,
                     side1 : Side,
                     index1 : int) -> bool:
        if index0 >= self.num_tracks:
            raise ValueError(f"Invalid index {index0}")
        if index1 >= self.num_tracks:
            raise ValueError(f"Invalid index {index1}")
        return side0 != side1 and index0 == index1

