Lesson 6: Introduction to Spiking Neural Networks (SNNs) 

6.1 How SNNs Mimic Biological Neurons 

Principle of SNNs: Spiking Neural Networks extend traditional neural networks by mimicking 
biological neuron activity, where information is transmitted through discrete spikes rather than 
continuous values. 

 Leaky Integrate-and-Fire Model: This model reflects how neurons integrate incoming 

signals until they reach a threshold: 

C_m dv/dt = I - (v - E_rest) 

 Physical Representation: This equation models a neuron's membrane potential over 
time, accounting for leaky current and input signals. 

6.2 Temporal Coding 

Information Representation: SNNs utilize both the timing of spikes and their frequency to 
encode information, providing a richer form of representation compared to traditional rates: 
 Precision Timing: The timing of each spike can convey distinct information, facilitating 
rapid responses in neural networks akin to biological systems. 

6.3 Applications in Real-Time Cognitive Modeling 

Real-Time Applications: SNNs are especially suited for problems that require quick reductions 
in processing time or interactive simulations, such as: 

 Sensory Processing: Quickly responding to environmental changes. 

 Real-Time Decision Making: Used in robotics or cognitive tasks where stimulus
response speed is critical. 

6.4 Hands-on Implementation: Train and Test a Simple SNN 

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
neurons = NeuronGroup(N, neuron_eqs, threshold='v > v_thresh', reset='v = 
v_leak', method='linear') 
neurons.v = v_leak 
# Input spikes simulate incoming stimuli 
input_spikes = PoissonGroup(N, rates=100 * Hz) 
S = Synapses(input_spikes, neurons, on_pre='v += 3 * mV') 
S.connect() 
# Monitoring spikes 
spike_mon = SpikeMonitor(neurons) 
run(100 * ms) 
# Plotting the spike activity 
plt.figure(figsize=(8, 4)) 
plt.plot(spike_mon.t/ms, spike_mon.i, '.k') 
plt.title('Spike Activity of Neurons in SNN') 
plt.xlabel('Time (ms)') 
plt.ylabel('Neuron Index') 
plt.show()
