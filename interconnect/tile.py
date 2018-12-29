class Tile():
    def __init__(self, num_inputs, num_outputs):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.core = None

    def set_core(self, core):
        self.core = core

    def inside(self, input):
        return 0 <= input < self.num_inputs

    def num_inputs(self) -> int:
        return self.core.num_inputs()

    def num_outputs(self) -> int:
        return self.core.num_outputs()

    def get_input(self, i):
        return self.core.get_input(i)

    def get_output(self, i):
        return self.core.get_output(i)
