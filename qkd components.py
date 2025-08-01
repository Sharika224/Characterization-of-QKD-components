# data generated through optisystem circuit
# INTENSITY MODULATOR"
import pandas as pd
import matplotlib.pyplot as plt
file_path = "intensity_modulator_data.csv"
data = pd.read_csv(file_path)
print("Data Preview:")
print(data.head())
if 'Input Voltage (V)' in data.columns and 'Output Power (mW)' in data.columns:
    plt.figure(figsize=(8, 5))
    plt.plot(data['Input Voltage (V)'], data['Output Power (mW)'], marker='o', label='Power Output')
    plt.title("Intensity Modulator Output Power vs Input Voltage")
    plt.xlabel("Input Voltage (V)")
    plt.ylabel("Output Power (mW)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# PHASE MODULATOR
def load_phase_modulator_data(file_path):
    df = pd.read_csv(file_path)
    print(df.head())
    return df
def plot_phase_modulator(df):
    plt.plot(df['Input Voltage (V)'], df['Interference Intensity (a.u.)'], marker='o')
    plt.title('Phase Modulator - Interference Intensity')
    plt.xlabel('Input Voltage (V)')
    plt.ylabel('Interference Intensity (a.u.)')
    plt.grid(True)
    plt.show()
phase_df = load_phase_modulator_data('phase_modulator_data.csv')
plot_phase_modulator(phase_df)


# QUANTUM CHANNEL
def load_quantum_channel_data(file_path):
    df = pd.read_csv(file_path)
    print(df.head())
    return df
def plot_quantum_channel(df):
    fig, ax1 = plt.subplots()
    ax1.plot(df['Fiber Length (km)'], df['Attenuation (dB)'], 'b-o', label='Attenuation')
    ax1.set_xlabel('Fiber Length (km)')
    ax1.set_ylabel('Attenuation (dB)', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2 = ax1.twinx()
    ax2.plot(df['Fiber Length (km)'], df['QBER (%)'], 'r-s', label='QBER')
    ax2.set_ylabel('QBER (%)', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    plt.title('Quantum Channel - Attenuation and QBER')
    plt.grid(True)
    plt.show()
channel_df = load_quantum_channel_data('quantum_channel_data.csv')
plot_quantum_channel(channel_df)


# SINGLE PHOTON DETECTOR
def load_spd_data(file_path):
    df = pd.read_csv(file_path)
    print(df.head())
    return df
def plot_spd_data(df):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs[0, 0].plot(df['Time (s)'], df['Dark Count Rate (cps)'], 'ko-')
    axs[0, 0].set_title('Dark Count Rate')
    axs[0, 0].set_xlabel('Time (s)')
    axs[0, 0].set_ylabel('Counts per second')
    axs[0, 1].plot(df['Time (s)'], df['Timing Jitter (ps)'], 'g^-')
    axs[0, 1].set_title('Timing Jitter')
    axs[0, 1].set_xlabel('Time (s)')
    axs[0, 1].set_ylabel('Jitter (ps)')
    axs[1, 0].plot(df['Time (s)'], df['Afterpulsing Probability (%)'], 'bs-')
    axs[1, 0].set_title('Afterpulsing Probability')
    axs[1, 0].set_xlabel('Time (s)')
    axs[1, 0].set_ylabel('Probability (%)')
    axs[1, 1].bar(df['Time (s)'], df['Detection Efficiency (%)'], color='purple')
    axs[1, 1].set_title('Detection Efficiency')
    axs[1, 1].set_xlabel('Time (s)')
    axs[1, 1].set_ylabel('Efficiency (%)')
    plt.tight_layout()
    plt.show()
spd_df = load_spd_data('single_photon_detector_data.csv')
plot_spd_data(spd_df)




