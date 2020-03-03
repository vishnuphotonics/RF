# This program plots two time domain & frequency domain plots 
from scipy import fftpack
import matplotlib.pyplot as ax
import numpy as np,time
f = 10  # Frequency, in cycles per second, or Hertz
f_s = 100  # Sampling rate, or number of measurements per second

t = np.linspace(0, 2, 2 * f_s, endpoint=False)
x = np.sin(f * 2 * np.pi * t)
X = fftpack.fft(x)
freqs = fftpack.fftfreq(len(x)) * f_s

fig, (ax1, ax2) = ax.subplots(1, 2)
fig.suptitle('Horizontally stacked subplots')
ax1.plot(t,x);ax2.plot(freqs, np.abs(X))
#ax.plot(freqs, np.abs(X))
ax.show(block=False)
ax.pause(3)
ax.close()

