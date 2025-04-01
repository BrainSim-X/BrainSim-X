import mne
import matplotlib.pyplot as plt

def load_eeg_data(file_path):
    raw = mne.io.read_raw_fif(file_path, preload=True)
    return raw

def filter_eeg_data(raw, l_freq=1.0, h_freq=40.0):
    raw.filter(l_freq=l_freq, h_freq=h_freq)

def plot_eeg(raw):
    raw.plot(duration=60, n_channels=30, scalings='auto')

if __name__ == "__main__":
    file_path = 'path_to_your_eeg_file.fif'
    raw_eeg = load_eeg_data(file_path)
    filter_eeg_data(raw_eeg)
    plot_eeg(raw_eeg)
