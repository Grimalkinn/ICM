# decibels.py
from time import ctime
import numpy as np
import matplotlib.pyplot as plt

def displayTerminationMessage():
    print('''
Programmed by Stew Dent.
Date: %s
End of Processing.''' % ctime())

def powerGain(maxPower, intervals):
    powers = np.linspace(1, maxPower, intervals+1)
    decibels = 20 * np.log10(powers)
    return powers, decibels

def voltageGain(maxVoltage, intervals):
    voltages = np.linspace(1, maxVoltage, intervals+1)
    decibels = 20 * np.log10(voltages)
    return voltages, decibels


def plotGain(units, gain, heading):
    plt.figure()
    plt.plot(units,gain,'r-')
    plt.xlabel(heading + ' (linear)')
    plt.ylabel('Decibels')
    plt.title(heading + ' Gain')
    plt.savefig(heading + 'Gain1.png')
    plt.show()
    
    plt.figure()
    plt.semilogx(units,gain,'r-')
    plt.xlabel(heading + ' (logarithmetic)')
    plt.ylabel('Decibels')
    plt.title(heading + ' Gain')
    plt.savefig(heading + 'Gain2.png')
    plt.show()


def main():
    maxPower = 10000
    maxVoltage = 10000
    intervals = 100000
    powers, powerGainDecibels =powerGain(maxPower, intervals)
    plotGain(powers, powerGainDecibels, 'Power')
    voltages, voltageGainDecibels =voltageGain(maxVoltage, intervals)
    plotGain(voltages, voltageGainDecibels,
            'Voltage')
    displayTerminationMessage()
    
main()
