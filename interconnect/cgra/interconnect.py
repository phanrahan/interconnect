from abc import ABC, abstractmethod
import enum
from .switchbox import SwitchBox

def manhattan_distance(i0, j0, i1, j1):
    return abs(i0 - i1) + abs(j0 - j1)

class Tile(ABC):
    def __init__(self, core, num_tracks):
        self.core = core
        for z in range(len(core.outputs)):
            self.sb[z] = SwitchBox(core.outputs[z], num_tracks)
            for i in range(len(core.inputs)):
                self.cb[z][i] = ConnectionBox(core.inputs, num_tracks)
            # connect connection box and switch box to tracks

    @abstractmethod
    def num_inputs(self) -> int:
        return self.core.num_inputs()

    @abstractmethod
    def num_outputs(self) -> int:
        return self.core.num_outputs()

class Interconnect(ABC):
    def __init__(self, core, num_tracks, nx, ny):
        self.nx = nx
        self.ny = ny
        for x in range(nx):
            for y = range(ny):
                self.tiles[x][y] = Tile(core, num_tracks)
        # wire up adjacent tiles
        for x in range(nx):
            for y = range(ny):
                pass

    @abstractmethod
    def size(self) -> (int, int):
        return (self.nx, self.ny)

    @abstractmethod
    def tile(self, i : int, j : int) -> Tile:
        pass

    @abstractmethod
    def is_connected(self,
                     tile0 : Tile,
                     side0 : Side,
                     index0 : int,
                     tile1 : Tile,
                     side1 : Side,
                     index1 : int) -> bool:
        pass
