import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
R = 20



df = pd.read_excel("3B6 data.xlsx")
print(df)

voltages = df['Voltage Probe Reading (V)'].tolist()
currents = (df['Current Probe Reading (V)']/R).tolist()
intensities = df['Photodiode Probe Reading (mV)'].tolist()
print(intensities)



plt.scatter(currents, intensities)
plt.show()