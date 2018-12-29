from abc import ABC, abstractmethod
from .tile import Tile

def manhattan_distance(i0, j0, i1, j1):
    return abs(i0 - i1) + abs(j0 - j1)

class Interconnect(ABC):
    def __init__(self, num_inputs, num_outputs, nx, ny):
        #self.num_inputs = num_inputs
        #self.num_outputs = num_outputs
        self.nx = nx
        self.ny = ny
        self.tiles = nx*[None]
        for x in range(nx):
            self.tiles[x] = ny*[None]
            for y in range(ny):
                self.tiles[x][y] = Tile(num_inputs, num_outputs)

    def size(self) -> (int, int):
        return (self.nx, self.ny)

    def inside(self, x: int, y: int) -> bool:
        nx, ny = self.size()
        return 0 <= x < nx and 0 <= y < ny

    def tile(self, x : int, y : int) -> Tile:
        return self.tiles[x][y]

    def get_input(self, x, y, i):
        return self.tile(x,y).get_input(i)

    def get_output(self, x, y, i):
        return self.tile(x,y).get_output(i)
