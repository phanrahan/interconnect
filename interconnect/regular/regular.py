from .. import Core, Tile, Switch, Interconnect, is_connected, connect

class Regular(Interconnect):
    def __init__(self, core, num_inputs, num_outputs, nx, ny):
        # generate nx, ny tiles and cores
        super().__init__(core, num_inputs, num_outputs, nx, ny)

        # connect each output to the inputs of its neighbors
        #  ** assumes core has one output **
        for x in range(nx):
            for y in range(ny):
                for z in range(num_inputs):
                    switch = Switch(8,1)
                    connect(switch.get_output(0), self.get_input(x,y,z))
                    for dx in [-1,0,1]:
                       for dy in [-1,0,1]:
                           if dx != 0 or dy != 0:
                                xp = x + dx
                                yp = y + dy
                                if 0 <= xp < nx and 0 <= yp < ny:
                                    print(f'connecting {xp,yp,0} {x,y,z}')
                                    connect( 
                                        self.get_output(xp,yp,0),
                                        switch.get_input(z) )

    def is_connectable(self, x0: int, y0: int, z0: int, 
                             x1: int, y1: int, z1: int) -> bool:
        output = self.get_output(x0,y0,z0).get_connection()
        for input in self.get_input(x1,y1,z1).connections():
            if switch.is_connectable(input, output):
                return True
        return False

    def is_connected(self,
                     x0: int,
                     y0: int,
                     output : int,
                     x1: int,
                     y1: int,
                     input : int) -> bool:
        pass
