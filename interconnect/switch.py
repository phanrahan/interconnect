from .port import Port

class Switch:
    def __init__(self, num_inputs, num_outputs):
        self.num_inputs = num_inputs
        self.inputs = [Port(self) for i in range(num_inputs)]
        self.num_outputs = num_outputs
        self.outputs = [Port(self) for i in range(num_outputs)]
        self.connection = None

    def get_input(self, i):
        assert 0 <= i < self.num_inputs
        return self.inputs[i]

    def get_output(self, i):
        assert 0 <= i < self.num_outputs
        return self.outputs[i]

    def is_connectable(self, input, output):
        return input in self.inputs and output in self.outputs

    def connect(self, input, output):
        self.connection = (input, output)

    def is_connected(self, input, output):
        return (input, output) == self.connection


