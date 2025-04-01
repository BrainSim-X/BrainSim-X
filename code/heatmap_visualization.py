import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def generate_heatmap(data):
    plt.figure(figsize=(12, 8))
    sns.heatmap(data, annot=True, cmap='coolwarm', cbar=True)
    plt.title('Neuroimaging Heatmap')
    plt.xlabel('Subjects')
    plt.ylabel('Brain Regions')
    plt.show()

if __name__ == "__main__":
    # Simulated dataset representing brain activity across subjects and regions
    data = np.random.rand(10, 12)  # 10 brain regions, 12 subjects
    generate_heatmap(data)
