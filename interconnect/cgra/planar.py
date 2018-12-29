from .. import Interconnect
from ..side import Side, opposite
#from .switchbox import SwitchBox

class Planar(Interconnect):
    def __init__(self, num_inputs, num_outputs, num_tracks, nx, ny):
        super().__init__(num_inputs, num_outputs, nx, ny)
        self.create_connections(nx, ny, num_tracks, num_inputs, num_outputs)

    def create_connections(self, nx, ny, num_tracks, num_inputs, num_outputs):
        # create switchbox
        #  connect to core outputs
        # create connection box
        #  connect to core inputs
        # connect switchbox to tracks
        pass

    def is_connectable(self,
                     tile0 : (int, int),
                     side0 : Side,
                     track0 : int,
                     tile1 : (int, int),
                     side1 : Side,
                     track1 : int) -> bool:

        if not self.inside(*tile0):
            raise ValueError(f"Invalid tile {tile0}")
        if not self.inside(*tile1):
            raise ValueError(f"Invalid tile {tile1}")

        if tile0[0] == tile1[0]:
             if side0 in (Side.SOUTH, Side.NORTH):
                 return side0 == opposite(side1) and track0 == track1
        if tile0[1] == tile1[1]:
             if side0 in (Side.EAST, Side.WEST):
                 return side0 == opposite(side1) and track0 == track1

        return False

