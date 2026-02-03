from models import deep, deep_cnn

import numpy as np
from sklearn.metrics import accuracy_score
from keras.callbacks import EarlyStopping

import pandas as pd
from dataset import DatasetGenerator

DIR = 'google_speech_commands' # unzipped train and test data
TEST_SET = 'test_set_X_y.csv' # csv with test set

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
df = dsGen.load_data(DIR, 37)
df_test = dsGen.load_test_set(DIR, TEST_SET, 37)
print(df.head())
print(df_test.head())

#dsGen.apply_train_test_split(test_size=0.3, random_state=2018)
dsGen.apply_train_val_split(val_size=0.15, random_state=37)


#==============================================================================
# Train
#==============================================================================              
model = deep_cnn(INPUT_SHAPE, NUM_CLASSES)
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['acc'])

early_stopper = EarlyStopping(
		monitor='val_loss',
		min_delta=0.001,
		patience=10,
		verbose=1,
		mode='min',
		restore_best_weights=True
)
history = model.fit(
			dsGen.generator(BATCH, mode='train'),
			steps_per_epoch=int(np.ceil(len(dsGen.df_train)/BATCH)),
			epochs=EPOCHS,
			verbose=1,
			validation_data=dsGen.generator(BATCH, mode='val'),
			validation_steps=int(np.ceil(len(dsGen.df_val)/BATCH)),
			callbacks=[early_stopper]
			)

history_df = pd.DataFrame(history.history)

#==============================================================================
# Predict
#==============================================================================

score = model.evaluate(dsGen.generator(BATCH, mode='test'), steps=int(np.ceil(len(dsGen.df_test)/BATCH)))

model.save('NEW_TEST_DATASET_model.keras')

print(score)
print(history_df)
history_df.to_csv("NEW_TEST_DATASET_training_history.csv", index=False)
