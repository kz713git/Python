import numpy as np
import wave_func as wf
import matplotlib.pyplot as plt
import random

#initialization
length = 2 ** 19

k = length
#k = int(k) + 1
x = random.random()
chaos = []

for i in range(1,k):
      
    if 0.05 <= x < 0.5:
        x = x + 2*x*x
    elif 0.5 <= x < 0.95:
        x = x - 2*(1-x)*(1-x)
    else:
        x = random.random()
    
    chaos.append(x*2-1)

fs = 48000
tmp = chaos 
#print(tmp)
S = np.fft.rfft(tmp)
#print(S)
fil = 1 / (np.arange(len(S))+1)
S = S * fil
s = np.fft.irfft(S)
s /= np.max(np.abs(s)*2)
wf.write_wave('./F_noise' +str(length)+ '.wav', s)

#visualize wave and fft
fig, ax = plt.subplots(nrows=2,figsize=(6.4, 4.8/0.96))
t = np.linspace(0, length/fs, length-2)
ax[0].plot(t, s, color="steelblue")
ax[0].set_title("Time domain")
ax[0].set_xlabel("Time[s]")
ax[0].set_ylabel("Amplitude")
#fig.tight_layout()
#plt.show()
S = np.fft.rfft(s)
#fig, ax = plt.subplots()
freq = np.linspace(0, fs/2, len(S))
ax[1].set_xscale("log")
ax[1].plot(freq, 20*np.log10(np.abs(S)), color="crimson")
ax[1].set_title("Frequency domain")
ax[1].set_xlabel("Frequency[Hz]")
ax[1].set_ylabel("Level[dB]")
fig.tight_layout()
fig.suptitle("1/f Noise")
fig.subplots_adjust(top=0.8, hspace=0.8)
plt.savefig('F Noize '+str(length)+'.png',dpi=300)
plt.show()
