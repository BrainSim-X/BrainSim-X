Lesson 1: Understanding Advanced Neural Dynamics 

1.1 Nonlinear Dynamics in Neural Computations 

Definition of Nonlinear Dynamics: Nonlinear dynamics refers to the behavior of systems in 
which outcomes are not directly proportional to their inputs. In neural terms, this indicates how 
the interaction between neurons and their signals leads to complex behaviors such as oscillations, 
bifurcations, and chaos—phenomena not observable in linear models. 

Mathematical Foundations: Neurons can be described using differential equations, particularly 
in models like the Hodgkin-Huxley model. Key equations of this model include: 

1. Membrane Potential Dynamics: 
2. C_m dv/dt = I_in - I_out 
o Where:  
 C_m is the membrane capacitance (reflects the neuron's ability to store 
charge). 
 I_in is the input current (coming from synapses). 
 I_out represents currents flowing out of the neuron. 
3. Ionic Currents: 
4. I_out = g_Na(m³)(h)(v - E_Na) + g_K(n⁴)(v - E_K) + g_L(v - E_L) 
o Where:  
 g_Na, g_K, and g_L are conductances for sodium, potassium, and leakage 
channels. 
 E_Na, E_K, and E_L are the respective reversal potentials for those 
channels. 
 m, n, and h are gating variables that represent the probability of channels 
being open. 
Biological Significance: 
 Neuronal Spiking: Spiking behavior arises when the membrane potential exceeds a 
certain threshold, resulting in an action potential. This is an example of a nonlinear 
response because it produces a specific output (spike) irrespective of a gradient of input 
prior to the threshold. 
 Signal Processing: Nonlinear dynamics allow for complex encoding of sensory 
information, enhancing the brain's computational capability.

1.2 Impact on Cognitive Processes 

Learning Mechanisms: 
 Hebbian Learning: 
o The principle that synaptic strength increases when the presynaptic and 
postsynaptic neurons are activated together. Mathematically, this can be 
represented by the update rule: 
 Δw_ij = η x_i y_j 
Where w_ij is the weight between neurons i and j, and η is the learning rate. 
o Biological Implication: As neurons relay signals, frequently used pathways 
strengthen, fostering memory and learning, exemplifying nonlinear adaptation in 
the neural network. 
 Synaptic Plasticity: 
o Long-Term Potentiation (LTP) and Long-Term Depression (LTD) articulate the 
mechanisms by which synapses strengthen or weaken. Importantly, these changes 
occur in a nonlinear manner; the changes in strength are not directly proportional 
to the number of action potentials but rather depend on the timing and order of 
neural firings.

1.3 Hands-on Implementation: Chaotic Neural Model 

Visualization of Nonlinear Dynamics: Utilizing the Lorenz attractor model illustrates 
nonlinear behavior through chaos. This model's chaotic patterns mimic communication dynamics 
within neuron clusters, capturing the essence of unpredictable neuronal firing patterns under 
varying stimuli. 

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters for the Lorenz system
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0

# Lorenz equations
def lorenz(state, t):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return np.array([dxdt, dydt, dzdt])

# Set initial conditions
initial_state = [0.0, 1.0, 1.05]
t = np.linspace(0, 40, 10000)
trajectory = odeint(lorenz, initial_state, t)

# 3D plot of Lorenz attractor
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], color='blue')

ax.set_title('Lorenz Attractor (Chaotic Dynamics)')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()
