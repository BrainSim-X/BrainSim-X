import numpy as np
import matplotlib.pyplot as plt

# Simulate real-time brain activity visualization
def visualize_brain_activity(data):
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()

    for i in range(len(data)):
        ax.clear()
        ax.imshow(data[i], cmap='viridis', aspect='auto')
        ax.set_title('Real-Time Brain Activity Visualization')
        plt.pause(0.1)

if __name__ == "__main__":
    # Simulating random brain activity data
    simulated_data = [np.random.rand(10, 10) for _ in range(100)]
    visualize_brain_activity(simulated_data)
