from models import deep, deep_cnn

from custom_callback import TimeHistory, InfoCallback

import numpy as np
from sklearn.metrics import accuracy_score
from keras.callbacks import EarlyStopping

import pandas as pd
from dataset import DatasetGenerator

DIR = 'input' # unzipped train and test data

INPUT_SHAPE = (177,98,1)
BATCH = 32
EPOCHS = 15

LABELS = 'down go left no right stop up yes'.split()
NUM_CLASSES = len(LABELS)

#==============================================================================
# Prepare data      
#==============================================================================
dsGen = DatasetGenerator(label_set=LABELS) 
# Load DataFrame with paths/labels for training and validation data 
# and paths for testing data 
df = dsGen.load_data(DIR)

dsGen.apply_train_test_split(test_size=0.3, random_state=2018)
dsGen.apply_train_val_split(val_size=0.3, random_state=2018)

print(df)

#==============================================================================
# Train
#==============================================================================              
model = deep_cnn(INPUT_SHAPE, NUM_CLASSES)
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['acc'])

timer = TimeHistory()
info = InfoCallback()
callbacks = [timer, info]

history = model.fit(dsGen.generator(BATCH, mode='train'),
                              steps_per_epoch=int(np.ceil(len(dsGen.df_train)/BATCH)),
                              epochs=EPOCHS,
                              verbose=1,
                              callbacks=callbacks,
                              validation_data=dsGen.generator(BATCH, mode='val'),
                              validation_steps=int(np.ceil(len(dsGen.df_val)/BATCH)))

history_df = pd.DataFrame(history.history)
history_df["batches_per_epoch"] = info.batch_counts
#history_df["steps_per_epoch"] = info.steps_counts
#history_df["samples_per_epoch"] = info.sample_counts
history_df["epoch_time_sec"] = timer.times

#==============================================================================
# Predict
#==============================================================================
score = model.evaluate(dsGen.generator(BATCH, mode='val'), steps=int(np.ceil(len(dsGen.df_val)/BATCH)))

model.save('RPM.keras')

print(score)
print(history_df)
history_df.to_csv("training_history.csv", index=False)
print("Total time:", timer.total_time)
