import pandas as pd
import matplotlib.pyplot as plt

# Load climate data
data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
    'Temperature': [15.2, 15.3, 15.4, 15.5, 15.6, 15.7, 15.8, 15.9, 16.0, 16.1, 16.2],
    'Rainfall': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
}
df = pd.DataFrame(data)

# Calculate rolling mean for temperature
df['Temperature_Rolling_Mean'] = df['Temperature'].rolling(window=3).mean()

# Plotting
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(df['Year'], df['Temperature'], marker='o', label='Temperature')
plt.plot(df['Year'], df['Temperature_Rolling_Mean'], linestyle='--', color='red', label='Rolling Mean (3 years)')
plt.title('Temperature Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(df['Year'], df['Rainfall'], marker='o', color='green')
plt.title('Rainfall Over Time')
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')

plt.tight_layout()
plt.show()

