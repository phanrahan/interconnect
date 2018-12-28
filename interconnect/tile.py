class Tile():
    def __init__(self, core):
        self.core = core

    def num_inputs(self) -> int:
        return self.core.num_inputs()

    def num_outputs(self) -> int:
        return self.core.num_outputs()

    def get_input(self, i):
        return self.core.get_input(i)

    def get_output(self, i):
        return self.core.get_output(i)
