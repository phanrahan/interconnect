import enum

class Side(enum.Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

def opposite(side):
    _opposite = {
        Side.NORTH: Side.SOUTH,
        Side.SOUTH: Side.NORTH,
        Side.EAST: Side.WEST,
        Side.WEST: Side.EAST,
    }
    return _opposite[side]

def is_opposite(side0, side1):
    return side0 == opposite(side1)

def rotate_cw(side):
    _rotate_cw = {
        Side.NORTH: Side.EAST,
        Side.EAST: Side.SOUTH,
        Side.SOUTH: Side.WEST,
        Side.WEST: Side.NORTH,
    }
    return _rotate_cw[side]

def rotate_ccw(side):
    _rotate_ccw = {
        Side.NORTH: Side.WEST,
        Side.WEST: Side.SOUTH,
        Side.SOUTH: Side.EAST,
        Side.EAST: Side.NORTH,
    }
    return _rotate[side]

