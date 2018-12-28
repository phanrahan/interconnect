import enum

class Side(enum.Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

opposite = {
    Side.NORTH: Side.SOUTH,
    Side.SOUTH: Side.NORTH,
    Side.EAST: Side.WEST,
    Side.WEST: Side.EAST,
}

def is_opposite(side0, side1):
    return side0 == opposite[side1]
