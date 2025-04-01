import numpy as np
import matplotlib.pyplot as plt

def simulate_neural_activity(num_neurons, time_steps):
    # Simulation of random neural firing activity
    activity = np.random.randn(num_neurons, time_steps)

    plt.figure(figsize=(12, 6))
    for neuron in range(num_neurons):
        plt.plot(activity[neuron], label=f'Neuron {neuron}')
    plt.title('Neural Activity Simulation')
    plt.xlabel('Time')
    plt.ylabel('Activity Level')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    simulate_neural_activity(num_neurons=5, time_steps=100)
