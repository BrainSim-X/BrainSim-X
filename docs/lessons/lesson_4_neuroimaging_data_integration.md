Lesson 4: Integrating High-Resolution Neuroimaging Data 

4.1 Neuroimaging Techniques 

Functional MRI (fMRI): fMRI measures brain activity by detecting changes in blood flow 
associated with neuronal activity (BOLD response). 

 BOLD Signal Dynamics: The BOLD response follows a hemodynamic response 
function (HRF):  

 h(t) = A · (t^(τ-1) e^(-t/τ))/(τ^τ Γ(τ)) 

o A represents the amplitude and Γ denotes the gamma function. 

EEG (Electroencephalography): EEG captures the electrical activity of the brain through 
electrodes placed on the scalp. This technique is characterized by high temporal resolution, 
making it suitable for real-time assessment of cognitive state transitions. 

PET (Positron Emission Tomography): PET imaging assesses metabolic processes in the brain 
using radioactive tracers. It provides insights into brain function and biochemical activity, while 
typically yielding lower temporal resolution than fMRI. 

4.2 Combining Multi-modal Datasets 
Data Fusion Strategies: Combining data from different neuroimaging modalities enhances 
understanding of neural processes. Three main strategies include: 

 Early Fusion: Combining raw data before analysis, integrating information at the initial 
stage. 

 Intermediate Fusion: Features extracted independently from different modalities are 
merged for joint analysis. 

 Late Fusion: Each modality is analyzed separately before integrating results for final 
outcomes. 

Neuroimaging Data Integration: Investigation into combined EEG-fMRI data can unlock 
insights into temporal brain activity: 

 Example: EEG data provides millisecond-level timing while fMRI offers spatial 
information, leading to deeper insights into brain networks during specific tasks or 
conditions. 

4.3 Hands-on Implementation: Preprocess and Visualize an EEG Dataset

import mne 
import matplotlib.pyplot as plt 
# Load EEG dataset (for instance, in .fif format) 
raw = mne.io.read_raw_fif('path_to_your_eeg_file.fif', preload=True) 
# Bandpass filter to isolate frequencies of interest 
raw.filter(l_freq=1.0, h_freq=40.0) 
# Detect events within the EEG data 
events = mne.find_events(raw) 
# Plotting raw EEG data 
raw.plot(duration=60, n_channels=30, scalings='auto') 
# Plotting detected events 
mne.viz.plot_events(events) 
plt.title('Detected Events in EEG Data') 
plt.show() 

This practical exercise provides a foundation for preprocessing EEG data, critical in analyzing 
tasks related to cognition.
