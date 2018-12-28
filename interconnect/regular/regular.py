from .. import Core, Tile, Switch, Interconnect, is_connectable, is_connected, connect

class Regular(Interconnect):
    def __init__(self, core, num_inputs, num_outputs, nx, ny):
        # generate nx, ny tiles and cores
        super().__init__(core, num_inputs, num_outputs, nx, ny)
        self.create_connections(nx, ny, num_inputs, num_outputs)

    def create_connections(self, nx, ny, nz, num_outputs):
        # connect each output to the inputs of its neighbors
        #  ** assumes core has one output **
        for x in range(nx):
            for y in range(ny):
                for z in range(nz):
                    self.create_connection(x, y, z, nx, ny)

    def create_connection(self, x, y, z, nx, ny):
        #print(f'connecting switch output{x,y,0} to input{x,y,z}')
        switch = Switch(8,1)
        connect(switch.get_output(0), self.get_input(x,y,z))
        switch_input = 0
        for dx in [-1,0,1]:
           for dy in [-1,0,1]:
               if dx != 0 or dy != 0:
                    xp = x + dx
                    yp = y + dy
                    if 0 <= xp < nx and 0 <= yp < ny:
                        #print(f'connecting output{xp,yp,0} to switch input{x,y,switch_input}')
                        connect( 
                            self.get_output(xp,yp,0),
                            switch.get_input(switch_input) )
                        switch_input += 1
                        #print(len(list(self.get_output(xp,yp,0).connections())))

    def is_connectable(self, x0: int, y0: int, z0: int, 
                             x1: int, y1: int, z1: int) -> bool:
        switch_output = self.get_input(x0,y0,z0).get_connection()
        for switch_input in self.get_output(x1,y1,z1).connections():
            if is_connectable(switch_input, switch_output):
                return True
            #if switch.is_connectable(output, input):
            #    return True
        return False

    def is_connected(self,
                     x0: int,
                     y0: int,
                     output : int,
                     x1: int,
                     y1: int,
                     input : int) -> bool:
        pass
