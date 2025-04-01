import numpy as np

# Example functions that simulate the core BrainSim-X functionalities
class BrainSimX:
    def __init__(self, neuron_count):
        self.neuron_count = neuron_count
        self.neurons = np.zeros(neuron_count)

    def activate_neuron(self, index, signal):
        if 0 <= index < self.neuron_count:
            self.neurons[index] += signal
            print(f"Neuron {index} activated with signal {signal}. Current value: {self.neurons[index]}")
        else:
            raise IndexError("Neuron index out of bounds")

if __name__ == "__main__":
    sim = BrainSimX(neuron_count=100)
    sim.activate_neuron(10, 0.5)  # Example usage
