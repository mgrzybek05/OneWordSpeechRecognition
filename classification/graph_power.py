import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 8})  # Set default font size to 12
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True

# Load CSV
pi_df = pd.read_excel(
    "C:/Work/f25/f25_datatest_testing/excel/power_measurements/raspi_7.xlsx")
stm_df = pd.read_excel(
    "C:/Work/f25/f25_datatest_testing/excel/power_measurements/kws_3.xlsx")

print(pi_df.head())
print(stm_df.head())

# Extract time and power columns
pi_time = pi_df["Time (s)"]
pi_power = pi_df["Main Avg Power (mW)"]

# remove after 16 seconds
pi_time = pi_time[pi_time < 16.0]
pi_power = pi_power[pi_time.index]

# remove first 3.8 seconds from pi data
pi_time = pi_time[pi_time > 3.8] - 3.8
pi_power = pi_power[pi_time.index]

stm_time = stm_df["Time (s)"]
stm_power = stm_df["Main Avg Power (mW)"]

# plot power consumption of pi
plt.figure(figsize=(3.5, 2.1), tight_layout=True)
plt.plot(pi_time, pi_power, color='orange')
plt.tight_layout()
plt.xlabel('Time (s)')
plt.ylabel('Power (mW)')
plt.xlim(5.5, 8.5)
plt.grid()
'''alpha = 0.15
plt.axvspan(0.20, 4.5, color='purple', alpha=alpha,
            label='loading')  # shade loading area
plt.axvspan(6.10, 7.86, color='blue', alpha=alpha,
            label='processing')  # shade processing area
plt.axvspan(9.4, 11, color='green', alpha=alpha,
            label='output')  # shade output area
plt.legend(fontsize=8, frameon=True, loc='upper left')'''
plt.savefig('pi_power.pdf', bbox_inches='tight')
plt.show()

# plot power consumption of stm32
plt.figure(figsize=(3.5, 2.1), tight_layout=True)
plt.plot(stm_time, stm_power, color='blue')
plt.tight_layout()
plt.xlabel('Time (s)')
plt.ylabel('Power (mW)')
plt.ylim(bottom=0)
plt.xlim(left=0, right=23)
plt.grid()
plt.savefig('stm_power.pdf', bbox_inches='tight')
plt.show()
