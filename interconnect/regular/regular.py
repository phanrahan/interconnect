from .. import Switch, Interconnect, is_connectable, is_connected, connect

class Regular(Interconnect):
    def __init__(self, num_inputs, num_outputs, nx, ny):
        # generate nx, ny tiles and cores
        super().__init__(num_inputs, num_outputs, nx, ny)
        #self.create_connections(nx, ny, num_inputs, num_outputs)

    def is_connectable(self, 
        tile0 : (int, int), track0: int, 
        tile1 : (int, int), track1: int) -> bool:

        if not self.inside(*tile0):
            raise ValueError(f"Invalid tile {tile0}")
        if not self.inside(*tile1):
            raise ValueError(f"Invalid tile {tile1}")
        if not self.tile(*tile0).inside(track0):
            raise ValueError(f"Invalid switch node track {(tile0, track0)}")
        if not self.tile(*tile1).inside(track1):
            raise ValueError(f"Invalid switch node track {(tile1, track1)}")

        if abs(tile0[0] - tile1[0]) > 1:
            return False

        if abs(tile0[1] - tile1[1]) > 1:
            return False

        return track0 == track1


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

    def connect(self, 
        tile0 : (int, int), track0: int, 
        tile1 : (int, int), track1: int) -> bool:
        pass

    def is_connected(self,
        tile0 : (int, int), track0: int, 
        tile1 : (int, int), track1: int) -> bool:
        pass
