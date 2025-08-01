import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.ensemble import IsolationForest

#Data is already given
# Intensity Modulator
intensity_data = pd.DataFrame({
    'Input Voltage (V)': np.linspace(0, 5, 10),
    'Output Power (mW)': [0.05, 0.2, 0.6, 1.0, 1.5, 1.7, 1.6, 1.2, 0.7, 0.1]
})
X1 = intensity_data[['Input Voltage (V)']]
y1 = intensity_data['Output Power (mW)']
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
model1 = make_pipeline(PolynomialFeatures(3), LinearRegression())
model1.fit(X1_train, y1_train)
y1_pred = model1.predict(X1_test)
r2_1 = r2_score(y1_test, y1_pred)
rmse_1 = mean_squared_error(y1_test, y1_pred) ** 0.5

plt.figure(figsize=(6, 4))
plt.scatter(X1, y1, color='blue', label='Actual')
plt.plot(X1.sort_values(by='Input Voltage (V)'), model1.predict(X1.sort_values(by='Input Voltage (V)')), color='red', label='Predicted')
plt.title('Intensity Modulator')
plt.xlabel('Input Voltage (V)')
plt.ylabel('Output Power (mW)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Phase Modulator
phase_data = pd.DataFrame({
    'Input Voltage (V)': np.linspace(0, 10, 20),
    'Phase Shift (rad)': np.linspace(0, 2 * np.pi, 20)
})
phase_data['Interference Intensity'] = 0.5 * (1 + np.cos(phase_data['Phase Shift (rad)']))
X2 = phase_data[['Input Voltage (V)']]
y2 = phase_data['Interference Intensity']
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
model2 = make_pipeline(PolynomialFeatures(4), LinearRegression())
model2.fit(X2_train, y2_train)
y2_pred = model2.predict(X2_test)
r2_2 = r2_score(y2_test, y2_pred)
rmse_2 = mean_squared_error(y2_test, y2_pred) ** 0.5

plt.figure(figsize=(6, 4))
plt.scatter(X2, y2, color='green', label='Actual')
plt.plot(X2.sort_values(by='Input Voltage (V)'), model2.predict(X2.sort_values(by='Input Voltage (V)')), color='orange', label='Predicted')
plt.title('Phase Modulator')
plt.xlabel('Input Voltage (V)')
plt.ylabel('Interference Intensity')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Quantum Channel
channel_data = pd.DataFrame({
    'Fiber Length (km)': np.arange(0, 55, 5),
    'Attenuation (dB)': np.arange(0, 55, 5) * 0.2
})
channel_data['QBER (%)'] = 1 + 0.05 * channel_data['Fiber Length (km)'] + np.random.normal(0, 0.05, len(channel_data))
X3 = channel_data[['Fiber Length (km)', 'Attenuation (dB)']]
y3 = channel_data['QBER (%)']
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)
model3 = LinearRegression()
model3.fit(X3_train, y3_train)
y3_pred = model3.predict(X3_test)
r2_3 = r2_score(y3_test, y3_pred)
rmse_3 = mean_squared_error(y3_test, y3_pred) ** 0.5

plt.figure(figsize=(6, 4))
plt.scatter(X3['Fiber Length (km)'], y3, color='purple', label='Actual')
plt.plot(X3['Fiber Length (km)'], model3.predict(X3), color='black', label='Predicted')
plt.title('Quantum Channel - QBER vs Fiber Length')
plt.xlabel('Fiber Length (km)')
plt.ylabel('QBER (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# SPD (Anomaly Detection)
spd_data = pd.DataFrame({
    'Time (s)': np.arange(0, 10),
    'Dark Count Rate (cps)': np.random.poisson(45, 10),
    'Detection Efficiency (%)': 65,
    'Timing Jitter (ps)': np.random.normal(60, 5, 10),
    'Afterpulsing Probability (%)': np.random.normal(0.5, 0.1, 10)
})
X4 = spd_data[['Dark Count Rate (cps)', 'Timing Jitter (ps)', 'Afterpulsing Probability (%)']]
model4 = IsolationForest(contamination=0.2, random_state=42)
anomaly_labels = model4.fit_predict(X4)
spd_data['Anomaly'] = anomaly_labels

plt.figure(figsize=(6, 4))
colors = ['red' if a == -1 else 'blue' for a in anomaly_labels]
plt.scatter(spd_data['Time (s)'], spd_data['Dark Count Rate (cps)'], c=colors)
plt.title('SPD Anomaly Detection')
plt.xlabel('Time (s)')
plt.ylabel('Dark Count Rate (cps)')
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nQKD Component ML Characterization Summary")
print(f"1. Intensity Modulator R² Score: {r2_1:.4f}")
print(f"   Intensity Modulator RMSE: {rmse_1:.4f} mW")
print(f"\n2. Phase Modulator R² Score: {r2_2:.4f}")
print(f"   Phase Modulator RMSE: {rmse_2:.4f}")
print(f"\n3. Quantum Channel R² Score: {r2_3:.4f}")
print(f"   Quantum Channel RMSE: {rmse_3:.4f}")
print(f"\n4. SPD Anomalies Detected: {list(anomaly_labels).count(-1)} / {len(anomaly_labels)} entries")


