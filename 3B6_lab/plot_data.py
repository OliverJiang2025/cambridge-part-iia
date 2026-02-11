import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
# resistance in TIR used to read current
R = 20

# read data from excel
df = pd.read_excel("3B6_lab/3B6 data.xlsx")
#print(df)

# load data
voltages = np.array(df['Voltage Probe Reading (V)'].tolist())
currents = np.array((df['Current Probe Reading (V)']/R*1000).tolist())
intensities = np.array(df['Photodiode Probe Reading (mV)'].tolist())
#print(intensities)

def plot_rawdata():
    fig, axs = plt.subplots(1, 2, figsize = (12,6))
    axs[0].scatter(currents, intensities)
    axs[0].set_title('Intensity - Current plot')
    axs[1].scatter(currents, voltages)
    axs[1].set_title('Voltage - Current plot')
    plt.show()

# linear fit of intensity - current
def linear_fit_1():
    new_intensities = intensities[:8]
    new_currents = currents[:8]
    k1, b1 = np.polyfit(new_currents, new_intensities, 1)
    return k1, b1, new_intensities, new_currents

def linear_fit_2():
    new_voltages = voltages[:-3]
    new_currents = currents[:-3]
    k2, b2 = np.polyfit(new_currents, new_voltages, 1)
    return k2, b2, new_voltages, new_currents

def plot_fit():
    k1, b1, new_intensities, new_currents_1 = linear_fit_1()
    k2, b2, new_voltages, new_currents_2 = linear_fit_2()

    fig, axs = plt.subplots(1, 2, figsize = (12,6))
    axs[0].scatter(currents, intensities, color = 'skyblue')
    axs[0].scatter(new_currents_1, new_intensities, color = 'skyblue')
    axs[0].plot(new_currents_1, k1*new_currents_1 + b1, color = 'orange')
    axs[0].set_title('Intensity - Current plot with linear fit')
    axs[0].set_xlabel('Current (mA)')
    axs[0].set_ylabel('Intensity (mV)')
    axs[0].text(10,400,f'Plot 1: k = {k1:.3f}, b = {b1:.3f}')

    axs[1].scatter(currents, voltages, color = 'skyblue')
    axs[1].scatter(new_currents_2, new_voltages, color = 'skyblue')
    axs[1].plot(new_currents_2, k2*new_currents_2 + b2, color = 'orange')
    axs[1].set_title('Voltage - Current plot with linear fit')
    axs[1].set_xlabel('Current (mA)')
    axs[1].set_ylabel('Voltage (V)')
    axs[1].text(10,2.85,f'Plot 2: 1000k = {k2*1000:.3f}, b = {b2:.3f}')
    
    plt.legend()
    plt.show()

if __name__ == '__main__':
    #plot_rawdata()
    plot_fit()