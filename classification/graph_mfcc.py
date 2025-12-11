import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 8}) # Set default font size to 12
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

cepPath = "C:/Work/s25_research_project/python/binaries/old/recordings/stop/stop_cep_10.bin"
sample_dtype = np.float32
dct_outputs = 13
stopFrame = 63
name = "MFCC"

with open(cepPath, "rb") as f:
    cepstrum_flat = np.fromfile(f, dtype=sample_dtype)

frames = len(cepstrum_flat) // dct_outputs
print(frames)

time_axis = np.linspace(0, 1, frames)
cepstrum = cepstrum_flat.reshape((frames, dct_outputs)).T

plt.figure(figsize=(3.5, 2.5), tight_layout=True)
plt.imshow(cepstrum, aspect='auto', origin='lower', extent=[time_axis[0], time_axis[-1], 0, 8000])
plt.colorbar()
plt.set_cmap('jet')
plt.xticks
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.savefig('mfcc.pdf', bbox_inches='tight')
plt.show()

