from qiskit import QuantumCircuit, Aer, execute
import matplotlib.pyplot as plt

def create_quantum_circuit():
    # Create a quantum circuit
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Apply Hadamard gate for superposition
    qc.measure(0, 0)  # Measure qubit state
    return qc

def simulate_quantum_circuit(qc):
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend=simulator, shots=1000).result()
    counts = result.get_counts()
    return counts

def plot_results(counts):
    plt.bar(counts.keys(), counts.values())
    plt.xlabel('Qubit State')
    plt.ylabel('Counts')
    plt.title('Quantum Neuron Output Distribution')
    plt.show()

# Main Functionality
if __name__ == "__main__":
    circuit = create_quantum_circuit()
    results = simulate_quantum_circuit(circuit)
    plot_results(results)
