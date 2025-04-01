from brian2 import *

# Define neuron parameters and equations
tau = 10 * ms
v_thresh = -50 * mV
v_leak = -65 * mV

# Neuron model dynamics
neuron_eqs = '''
dv/dt = (v_leak - v) / tau : volt
'''

# Create a population of spiking neurons
N = 100  # Number of neurons
neurons = NeuronGroup(N, neuron_eqs, threshold='v > v_thresh', reset='v = v_leak', method='linear')
neurons.v = v_leak

# Input spikes simulate incoming stimuli
input_spikes = PoissonGroup(N, rates=100 * Hz)
S = Synapses(input_spikes, neurons, on_pre='v += 3 * mV')
S.connect()

# Monitoring spikes
spike_monitor = SpikeMonitor(neurons)
run(100 * ms)

# Plotting the spike activity
plt.figure(figsize=(8, 4))
plt.plot(spike_monitor.t/ms, spike_monitor.i, '.k')
plt.title('Spike Activity of Neurons in SNN')
plt.xlabel('Time (ms)')
plt.ylabel('Neuron Index')
plt.show()
