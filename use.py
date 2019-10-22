from keras.models import load_model
from numpy import array, asarray, shape

from dataset import DatasetGenerator

model = load_model('yes_no_up.h5')

LABELS = 'down go left no one right stop two up yes'.split()
dsGen = DatasetGenerator(label_set=LABELS) 

x = array(dsGen.process_wav_file('input/yes/0a7c2a8d_nohash_0.wav'))
#x = array(dsGen.process_wav_file('input/no/0a9f9af7_nohash_0.wav'))
#x = array(dsGen.process_wav_file('input/up/0a7c2a8d_nohash_0.wav'))
x = asarray(x).reshape(-1, 177, 98, 1)

# make a prediction
y = model.predict(x)
prediction = y[0]

if prediction[0] > 0.99:
    print('wake up')
else:
    print('still asleep...')