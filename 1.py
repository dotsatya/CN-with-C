# 1.	Implement Manchester Encoding and Differential Manchester Encoding for the binary data 1011100010. Provide screenshot of the output generated. Note the result and draw the corresponding timing diagram for the resultant waveform. 
#Manchester Encoding

import matplotlib.pyplot as plt
import numpy as np
data = input ("Data : ")
print("Original Data")
print(data)

def manchester_encode(d):
    m = ""
    e = []
    for bit in d:
        e.extend([0,1] if bit=="1" else [1,0])
        m += ("[01]" if bit=="1" else "[10]")
    return (e, m)
def diff_manchester_encode(d):
    dm = ""
    e = []
    prev = 1
    for bit in d:
        dm += "["
        if bit=="0":
            prev = 1 - prev
            e.append(prev)
            dm +=str(prev)
        else:
            e.append(prev)
        mid = 1 - e[-1]
        e.append(mid)
        dm += str(mid)
        prev = e[-1]
        dm += "]"
    return (e, dm)
(m_enc, m) = manchester_encode(data)
(dm_enc, dm) = diff_manchester_encode(data)
print("Manchester Encoding:")
print(m)
print("Differential Manchester Encoding:")
print(dm)

original_bits = [int(bit) for bit in data]
original_plot_data = []
for bit in original_bits:
    original_plot_data.extend([bit, bit])

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
t = np.arange(0, len(m_enc))

axes[0].step(t, original_plot_data, where='post')
axes[0].set_ylim(-0.5, 1.5)
axes[0].set_yticks([0, 1])
axes[0].set_title("Original Data")
axes[0].set_ylabel("Signal Level")
axes[0].grid(True)

axes[1].step(t, m_enc, where='post')
axes[1].set_ylim(-0.5, 1.5)
axes[1].set_yticks([0, 1])
axes[1].set_title("Manchester Encoding")
axes[1].set_xlabel("Time")
axes[1].set_ylabel("Signal Level")
axes[1].grid(True)

bit_positions = np.arange(0, len(m_enc)+1, 2)
plt.xticks(bit_positions)
for ax in axes:
    ax.grid(True, which='major', axis='x')
    ax.set_xticks(bit_positions, minor=False)

plt.tight_layout()
plt.savefig("manchester_encoding.png")
plt.show()

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
t = np.arange(0, len(dm_enc))

axes[0].step(t, original_plot_data, where='post')
axes[0].set_ylim(-0.5, 1.5)
axes[0].set_yticks([0, 1])
axes[0].set_title("Original Data")
axes[0].set_ylabel("Signal Level")
axes[0].grid(True)

axes[1].step(t, dm_enc, where='post')
axes[1].set_ylim(-0.5, 1.5)
axes[1].set_yticks([0, 1])
axes[1].set_title("Differential Manchester Encoding")
axes[1].set_xlabel("Time")
axes[1].set_ylabel("Signal Level")
axes[1].grid(True)

bit_positions = np.arange(0, len(dm_enc)+1, 2)
plt.xticks(bit_positions)
for ax in axes:
    ax.grid(True, which='major', axis='x')
    ax.set_xticks(bit_positions, minor=False)

plt.tight_layout()
plt.savefig("diff_manchester_encoding.png")
plt.show()