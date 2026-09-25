import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sample_rate = 100
duration = 5

num_samples = int(sample_rate * duration)
print(f"Number of samples: {num_samples}")

time = np.linspace(0.00, 4.99, num_samples, dtype=float)
print(f"First timestamp: {time[0]}")
print(f"Last timestamp: {time[-1]}")
print(f"Number of timestamps: {len(time)}")

temperature = 25 + np.random.normal(0, 0.5, size=num_samples)
print(f"Temperature mean: {temperature.mean():.2f} °C")
print(f"Temperature minimum: {temperature.min():.2f} °C")
print(f"Temperature maximum: {temperature.max():.2f} °C")

voltage = 12 + np.random.normal(0, 0.1, size=num_samples)
print(f"Voltage mean: {voltage.mean():.2f} V")
print(f"Voltage minimum: {voltage.min():.2f} V")
print(f"Voltage maximum: {voltage.max():.2f} V")
print(f"Voltage number of samples: {len(voltage)}")

current = 2 + np.random.normal(0, 0.05, size=num_samples)
print(f"Current mean: {current.mean():.2f} A")
print(f"Current minimum: {current.min():.2f} A")
print(f"Current maximum: {current.max():.2f} A")
print(f"Current number of samples: {len(current)}")

pressure = 1.0 + np.random.normal(0, 0.02, size=num_samples)
print(f"Pressure mean: {pressure.mean():.2f} bar")
print(f"Pressure minimum: {pressure.min():.2f} bar")
print(f"Pressure maximum: {pressure.max():.2f} bar")
print(f"Pressure number of samples: {len(pressure)}")

data = pd.DataFrame({
    'timestamp': time,
    'temperature': temperature,
    'voltage': voltage,
    'current': current,
    'pressure': pressure
})

print(data.head())
print(data.shape)
print(data.describe())

plt.subplot(2, 2, 1)
plt.plot(data['timestamp'], data['temperature'], color='red')
plt.title('Temperature (°C)')

plt.subplot(2, 2, 2)
plt.plot(data['timestamp'], data['voltage'], color='blue')
plt.title('Voltage (V)')

plt.subplot(2, 2, 3)
plt.plot(data['timestamp'], data['current'], color='green')
plt.title('Current (A)')

plt.subplot(2, 2, 4)
plt.plot(data['timestamp'], data['pressure'], color='orange')
plt.title('Pressure (bar)')

plt.tight_layout()
plt.show()