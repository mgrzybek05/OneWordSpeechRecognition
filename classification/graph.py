import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams.update({'font.size': 8})  # Set default font size to 12
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True

df = pd.read_csv("NEW_TEST_DATASET_training_history.csv")
acc = list(df['acc'])
loss = list(df['loss'])
val_acc = list(df['val_acc'])
val_loss = list(df['val_loss'])

plt.figure(figsize=(3.5, 2.8), tight_layout=True)
plt.plot(range(1, 16), acc, label='Training Accuracy', color='r')
plt.plot(range(1, 16), val_acc, label='Validation Accuracy', color='g')
plt.legend(loc='best')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.yticks(np.linspace(0, 1, 21))
plt.xticks(list(range(1, 16)))
plt.ylim(bottom=0.6, top=1)
plt.grid(True)
plt.savefig('accuracy_new_dataset.pdf', bbox_inches='tight')
plt.close()

plt.figure(figsize=(3.5, 2.8), tight_layout=True)
plt.plot(range(1, 16), loss, label='Training Loss', color='r')
plt.plot(range(1, 16), val_loss, label='Validation Loss', color='g')
plt.legend(loc='best')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.ylim(0, 3.5)
plt.xticks(list(range(1, 16)))
plt.grid(True)
plt.savefig('loss_new_dataset.pdf', bbox_inches='tight')
plt.close()
