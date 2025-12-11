import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

plt.rcParams.update({'font.size': 8}) # Set default font size to 12
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.top'] = False
plt.rcParams['ytick.right'] = False

# Load CSV
dt_pi = pd.read_csv("dataframe.csv")

df_stm = pd.read_excel("C:/Work/f25/f25_datatest_testing/python/output/results_kws_3V3.xlsx")

df_stm_2 = pd.read_csv("C:/Work/f25/class.csv")

# Compute confusion matrix
pi_cm = confusion_matrix(dt_pi["label"], dt_pi["prediction"])
stm_cm = confusion_matrix(df_stm["keyword"], df_stm["prediction"])

cm = df_stm_2.drop(columns=['Keyword']).to_numpy()
print(cm)

labels = ["down", "go", "left", "no", "right", "stop", "up", "yes"]

# Display
disp = ConfusionMatrixDisplay(confusion_matrix=pi_cm, display_labels=labels)
disp.plot(cmap="Blues")
ax = plt.gca()
ax.figsize = (3.5, 2.5)
plt.savefig('pi_confusion_matrix.pdf', bbox_inches='tight')
plt.show()

disp = ConfusionMatrixDisplay(confusion_matrix=stm_cm, display_labels=labels)
disp.plot(cmap="Blues")
ax = plt.gca()
ax.figsize = (3.5, 2.5)
plt.savefig('stm_confusion_matrix.pdf', bbox_inches='tight')
plt.show()

labels = ["Down", "Go", "Left", "No", "Right", "Stop", "Up", "Yes", "Noise"]

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
disp.plot(cmap="Blues")
ax = plt.gca()
plt.savefig('stm_2_confusion_matrix.pdf', bbox_inches='tight')
plt.show()
