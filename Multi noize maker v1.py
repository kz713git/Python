import numpy as np
import wave_func as wf
import matplotlib.pyplot as plt
import random

#initialization

fs = 48000
length = 2 ** 17

#------------
#White Noise
s = np.random.random(size=length)*2 - 1
wf.write_wave('./white_noise' +str(length)+ '.wav', s)

#visualize wave and fft
fig, ax = plt.subplots(nrows=2,figsize=(6.4, 4.8/0.96))
t = np.linspace(0, length/fs, length)
ax[0].plot(t, s, color='steelblue')
ax[0].set_title('Time domain')
ax[0].set_xlabel('Time[s]')
ax[0].set_ylabel('Amplitude')

S = np.fft.rfft(s)
freq = np.linspace(0, fs/2, len(S))

ax[1].set_xscale('log')
ax[1].plot(freq, 20*np.log10(np.abs(S)), color='crimson')
ax[1].set_title('Frequency domain')
ax[1].set_xlabel('Frequency[Hz]')
ax[1].set_ylabel('Level[dB]')
fig.tight_layout()
fig.subplots_adjust(top=0.8, hspace=0.8)
fig.suptitle('White Noise', size=15)

plt.savefig('White Noize '+str(length)+'.png',dpi=300)
#plt.show()

#------------
#Pink Noise
tmp = np.random.random(size=length)*2 - 1
S = np.fft.rfft(tmp)

fil = 1 / (np.arange(len(S))+1)
S = S * fil
s = np.fft.irfft(S)
s /= np.max(np.abs(s))
wf.write_wave('./Pink_noise' +str(length)+ '.wav', s)

#visualize wave and fft
fig, ax = plt.subplots(nrows=2,figsize=(6.4, 4.8/0.96))
t = np.linspace(0, length/fs, length)
ax[0].plot(t, s, color='steelblue')
ax[0].set_title('Time domain')
ax[0].set_xlabel('Time[s]')
ax[0].set_ylabel('Amplitude')

S = np.fft.rfft(s)
freq = np.linspace(0, fs/2, len(S))

ax[1].set_xscale('log')
ax[1].plot(freq, 20*np.log10(np.abs(S)), color='crimson')
ax[1].set_title('Frequency domain')
ax[1].set_xlabel('Frequency[Hz]')
ax[1].set_ylabel('Level[dB]')
fig.tight_layout()
fig.subplots_adjust(top=0.8, hspace=0.8)
fig.suptitle('Pink Noise', size=15)

plt.savefig('Pink Noize '+str(length)+'.png',dpi=300)

#------------
#1/f Noise

#initialization
k = length
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

tmp = chaos 
S = np.fft.rfft(tmp)
fil = 1 / (np.arange(len(S))+1)
S = S * fil
s = np.fft.irfft(S)
s /= np.max(np.abs(s)*2)
wf.write_wave('./F_noise' +str(length)+ '.wav', s)

#visualize wave and fft
fig, ax = plt.subplots(nrows=2,figsize=(6.4, 4.8/0.96))
t = np.linspace(0, length/fs, length-2)
ax[0].plot(t, s, color='steelblue')
ax[0].set_title('Time domain')
ax[0].set_xlabel('Time[s]')
ax[0].set_ylabel('Amplitude')

S = np.fft.rfft(s)
freq = np.linspace(0, fs/2, len(S))

ax[1].set_xscale('log')
ax[1].plot(freq, 20*np.log10(np.abs(S)), color='crimson')
ax[1].set_title('Frequency domain')
ax[1].set_xlabel('Frequency[Hz]')
ax[1].set_ylabel('Level[dB]')
fig.tight_layout()
fig.subplots_adjust(top=0.8, hspace=0.8)
fig.suptitle('1/f Noise', size=15)

plt.savefig('F Noize '+str(length)+'.png',dpi=300)
plt.show()
