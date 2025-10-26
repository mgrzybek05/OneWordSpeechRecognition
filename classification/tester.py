from keras.models import load_model
from numpy import array, asarray, shape
import numpy as np
from dataset import DatasetGenerator
import random
from keras.utils import to_categorical
import time


MODEL_DIR = 'RPM.keras'
DIR = 'testing_set'
BATCH = 32

def main():
    model = load_model(MODEL_DIR)
    LABELS = 'down go left no right stop up yes'.split()
    dsGen = DatasetGenerator(label_set=LABELS) 
    df = dsGen.load_data(DIR)
    num_utterances = len(list(range(df.shape[0])))

    start_time = time.time()
    loss, accuracy = model.evaluate(batch_gen(dsGen, BATCH), steps=int(np.ceil(len(dsGen.df)/BATCH)))
    delay_ms = (time.time() - start_time)*1000
  
    print(f"Loss: {loss} \nAccuracy: {accuracy}\nItems: {num_utterances}\nDelay: {delay_ms}\nDelay Per: {delay_ms/num_utterances}")

    return 0

def batch_gen(dsGen, batch_size):
    while True:
        # Depending on mode select DataFrame with paths
        df = dsGen.df
        ids = list(range(df.shape[0]))

        # Create batches (for training data the batches are randomly permuted)
        for start in range(0, len(ids), batch_size):
            X_batch = []
            y_batch = []
            end = min(start + batch_size, len(ids))
            i_batch = ids[start:end]
            for i in i_batch:
                X_batch.append(dsGen.process_wav_file(df.wav_file.values[i]))
                y_batch.append(df.label_id.values[i])
            X_batch = np.array(X_batch)

            y_batch = to_categorical(y_batch, num_classes = len(dsGen.label_set))
            yield (X_batch, y_batch)
 

if __name__ == '__main__':
    main()